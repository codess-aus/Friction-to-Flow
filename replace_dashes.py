import os
import re

EM_DASH = '\u2014'

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if EM_DASH not in content:
        return 0, 0
    
    lines = content.splitlines(keepends=True)
    new_lines = []
    replacements_in_file = 0
    
    for line in lines:
        original_line = line
        
        if line.strip().startswith('#'):
            # Rule 1: Heading
            # Handle ' — ', ' —', '— ' -> ' - '
            # We also handle '—' just to be safe and consistent with "Otherwise" logic? 
            # No, let's follow the prompt strictly.
            # Prompt: "replace ' — ' with ' - '. Also handle ' —' or '— ' edge cases by replacing with ' - '."
            line = line.replace(f' {EM_DASH} ', ' - ')
            line = line.replace(f'{EM_DASH} ', ' - ')
            line = line.replace(f' {EM_DASH}', ' - ')
            # What if it's just '—'? The prompt didn't say. 
            # But the Rule 3 says "Otherwise... replace '—' with ', '".
            # If I don't handle '—' in headings here, Rule 3 is "Otherwise", 
            # but Rule 1 is an "If". 
        else:
            # Rule 2: Inside bold **...**
            # Find all bold sections
            def bold_replacer(match):
                # Prompt: "replace ' — ' with ' - '"
                return match.group(0).replace(f' {EM_DASH} ', ' - ')
            
            line = re.sub(r'\*\*.*?\*\*', bold_replacer, line)
            
            # Rule 3: Otherwise (regular prose)
            # "replace ' — ' with ', ' (comma + space). If the em dash isn't surrounded by spaces, replace '—' with ', '."
            line = line.replace(f' {EM_DASH} ', ', ')
            line = line.replace(EM_DASH, ', ')
            
        replacements_in_file += (original_line.count(EM_DASH) - line.count(EM_DASH))
        new_lines.append(line)
    
    if replacements_in_file > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return 1, replacements_in_file
    return 0, 0

def main():
    total_files = 0
    total_replacements = 0
    for root, dirs, files in os.walk('docs'):
        for file in files:
            if file.endswith('.md'):
                f_mod, r_count = process_file(os.path.join(root, file))
                total_files += f_mod
                total_replacements += r_count
                
    print(f"Files modified: {total_files}")
    print(f"Total replacements: {total_replacements}")

if __name__ == "__main__":
    main()
