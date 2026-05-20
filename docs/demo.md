# Demo - GitHub Copilot Coding Agents in Action

<div class="f2f-video" markdown>
<video controls preload="metadata" playsinline
       aria-label="GitHub Copilot Coding Agents demo video">
  <source src="../assets/AgentsDemo.mp4" type="video/mp4">
  Your browser does not support embedded video. You can
  <a href="../assets/AgentsDemo.mp4">download the demo (MP4)</a> instead.
</video>
</div>

## What GitHub Copilot Coding Agents are

*(Snapshot of the feature set as of April–May 2026. Capabilities change
quickly, check the official
[GitHub Copilot docs](https://docs.github.com/en/copilot) for the current
state.)*

GitHub Copilot has grown from an in-editor pair-programmer into a family
of **agentic experiences** that span the IDE, github.com, mobile, and CLI.
The piece this demo focuses on is the **coding agent**, an autonomous
worker you can hand a task to and walk away from.

### Where you can launch an agent

| Surface | Trigger | Best for |
| --- | --- | --- |
| **github.com** | Assign an issue to `@copilot`, or click *Start coding with Copilot* on an issue | Well-scoped tickets, parallel work while you do something else |
| **VS Code / JetBrains / Visual Studio** | Switch Copilot Chat into **Agent mode** | Multi-step tasks in your local checkout, with you watching |
| **GitHub Mobile** | Kick off a task from an issue on your phone | Triage on the train; the work runs in the cloud |
| **GitHub CLI** | `gh copilot` agentic commands | Scripting, batch tasks, CI integrations |
| **Copilot Workspace** | Open an issue, refine a spec + plan, then execute | When you want to steer the plan before code is written |

### How a cloud-based coding agent task runs

1. **You assign a task.** Usually an issue, sometimes a comment on an
   existing PR ("address these review notes"), sometimes a free-form
   prompt.
2. **The agent spins up an ephemeral, sandboxed environment.** It clones
   the repo onto a fresh runner with the network policy you configured.
3. **It plans, edits, and runs.** It reads the code, makes changes across
   files, runs your build, your tests, your linters, your scanners, all
   the things your CI normally runs.
4. **It opens a draft pull request.** The PR description includes the
   plan, the diff summary, the commands it ran, and the results.
5. **You review.** Comment on lines, request changes, push your own
   commits on top, or close it and try again with a sharper prompt.
6. **You merge.** The agent never merges itself. Branch protections,
   required reviews, required checks, and CODEOWNERS all still apply.

### What's new in the April / May 2026 timeframe

The themes the GitHub team has been pushing in recent releases:

- **Better planning before code.** Agents now produce an explicit
  step-by-step plan and a list of files they expect to touch *before*
  they start editing, so you can correct course early.
- **MCP everywhere.** Coding agents speak the
  [Model Context Protocol](https://modelcontextprotocol.io/), so you can
  give them access to your internal docs, ticketing system, observability
  stack, or any other MCP server, under policies you control.
- **`AGENTS.md` as a first-class concept.** A repo-level file that tells
  agents how this codebase wants to be worked on: build commands,
  conventions, no-go areas, review expectations. Treated as durable
  guidance, not a system prompt.
- **Parallel agents.** You can run multiple coding agents at once against
  the same repo, typically one per task, and they each get isolated
  branches and PRs.
- **Org-level policy and governance.** Admins can scope which repos can
  use coding agents, control network egress from agent sandboxes, set
  spending limits (agents consume GitHub Actions minutes), and audit
  every action.
- **Tighter review-loop ergonomics.** Re-prompting an agent by commenting
  `@copilot fix the failing test` on its PR; agents responding to review
  comments with new commits; agents updating their own PR descriptions
  as the change evolves.

> Cross-check anything specific against the official **GitHub Changelog**
> and **Copilot release notes** before quoting it on stage. Feature names
> and limits move month-to-month.

---

## What coding agents are good at

The honest list, based on actually using them.

- **Boilerplate and scaffolding.** New DTO, repository class, route,
  CRUD endpoint, test fixture, the agent flies through these.
- **Repetitive refactors across many files.** Renaming, extracting,
  migrating from one pattern to another, updating call sites after an
  API change.
- **Test scaffolds.** Drafting the obvious unit / integration test
  cases against a function you already wrote. You still curate which
  tests are actually meaningful.
- **Dependency hygiene and small upgrades.** Bumping a library and
  fixing the obvious breakage; cleaning up unused imports; aligning
  versions across a monorepo.
- **Doc drafts.** READMEs, API references, runbooks, first drafts
  that you sharpen.
- **Issue triage and reproduction.** "Try to reproduce this bug in a
  test." The agent will often write a failing test that captures the
  problem, even if it can't fix it yet.
- **Mechanical fixes from a scan.** Address a code-scanning alert, a
  Dependabot PR, or a Copilot autofix suggestion across the codebase.

## What you should not hand over

The parts that need a human in the seat:

- **Architecture decisions.** Module boundaries, data model design,
  framework choice, these need context the agent does not have.
- **Anything user-facing without taste.** Copy, UX, naming, accessibility
  judgement.
- **Security-critical code paths.** Auth, crypto, payment, data egress.
  An agent can draft; a human signs off.
- **Production data and secrets.** Never paste them into prompts; do not
  give the agent runtime access to live systems unless the policy is
  designed for it.
- **Anything where being wrong is expensive and hard to detect.** The
  agent is fast and confident, that is exactly when you need to slow
  down and verify.

---

## A practical playbook

A short, opinionated guide to getting useful work out of coding agents
without losing control.

### Set the table once, benefit forever

1. **Write a clear `AGENTS.md`** at the repo root. Build commands, test
   commands, conventions, "do not touch" directories, definition of done.
2. **Pin a `copilot-instructions.md`** with codebase-specific guidance
   (style, error handling, logging, naming).
3. **Keep CI honest.** Lint, type-check, unit, integration, security
   scans, all required, all blocking. The agent benefits from a fast,
   strict CI more than anyone, because it iterates against it.
4. **Configure branch protections.** Require reviews. Require checks.
   Require signed commits where it matters. The agent must play by the
   same rules as a human.

### Hand off a task well

- **Scope it small.** "Add a `/health` endpoint with a test" beats
  "improve observability."
- **Be explicit about acceptance.** What does *done* look like? Which
  tests prove it?
- **Point at examples.** "Follow the pattern in `src/foo/bar.ts`."
- **Name the constraints.** Don't change public APIs. Don't touch the
  database migration files. Don't add new dependencies.

### Review like the adult in the room

- **Read every line.** No skimming agent PRs. They look polished; that
  is the danger.
- **Ask why.** Drop a review comment asking the agent to justify a
  non-obvious choice. The answer often reveals a misunderstanding.
- **Rewrite freely.** Push your own commits onto its branch when the
  fastest path forward is to fix it yourself.
- **Reject without guilt.** Closing an agent PR and starting again with
  a sharper prompt is a normal, healthy outcome.

### Govern the fleet

- **Watch your minutes.** Coding agents burn GitHub Actions time. Set
  org-level limits.
- **Restrict egress.** Agent sandboxes should not be able to reach
  whatever they want on the internet. Allow-list what they need.
- **Audit.** Treat agent activity as a first-class log source. Who ran
  what, against which repo, on what data.
- **Disclose.** If a process owner needs to know an agent contributed
  to a change, tell them.

---

## The bottom line

GitHub Copilot coding agents are **fast, literal, tireless teammates**.
They will take the toil off your plate at a scale that genuinely changes
what one developer can ship. They will not protect your job, and they
will not protect your codebase. **You** do that, by bringing judgement,
creativity, oversight, and ownership to every PR they open.

Partner with them. Don't outsource to them. Stay in the loop. Own the
code.

That's the whole game.

<!--
Speaker note: the demo runs ~2 minutes. After it plays, restate three
points:
  1. The agent is gated by the same PR + branch-protection rules as
     humans.
  2. The interesting unlock is *parallel* agents on small, well-scoped
     tasks, not one big agent on one big task.
  3. Governance (AGENTS.md, network policy, action minutes, audit) is
     what makes this safe to run at org scale.
-->
