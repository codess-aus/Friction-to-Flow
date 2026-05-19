# Friction-to-Flow

A talk and accompanying website: *How GitHub Copilot transformed my
daily workflow and amplified my impact.*

## Site

The site is published with **MkDocs Material** from the `docs/` folder
and deployed to **GitHub Pages** by the workflow in
`.github/workflows/deploy.yml`.

- Strict high-contrast palette (pure black-on-white / white-on-black, no
  greys) for accessibility
- Cyan → blue → purple brand gradient on header, tabs, rules, and cards
- Light / dark mode toggle in the header
- Fully responsive

### Enable GitHub Pages

In **Settings → Pages**, set *Source* to **GitHub Actions**. Push to
`main` and the site will deploy automatically.

### Run locally

```bash
pip install mkdocs-material pymdown-extensions
mkdocs serve
```

Then open http://127.0.0.1:8000/.

## Structure

```
mkdocs.yml                     # site config
docs/
  index.md                     # landing page
  01-friction-to-flow.md ... 14-close.md
  demo.md                      # video + Copilot Coding Agents content
  assets/                      # slide PNGs + AgentsDemo.mp4
  stylesheets/extra.css        # gradient + high-contrast theme overrides
.github/workflows/deploy.yml   # Pages deployment
```

Speaker notes live as HTML comments at the bottom of each chapter
markdown — visible in the source on GitHub, hidden on the rendered site.
