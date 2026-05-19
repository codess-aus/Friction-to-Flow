![Responsible AI](assets/11-responsible.png){ .hero }

# Chapter 11 — Responsible AI

> *I own the code. Not the model. Not the vendor. Me.*

Let me be unambiguous about responsibility, because the industry tends to get vague here and vague is dangerous.

When code I shipped causes a problem — a bug, an outage, a security incident, a biased outcome, a data leak — **I am responsible.** Not Copilot. Not the agent. Not the model. Me. My name is on the commit. My name is on the PR. My judgement signed off.

That responsibility shapes how I use the tool:

- **Oversight is non-negotiable.** I do not merge code I haven't understood. "The AI wrote it" is not an explanation; it's an excuse, and excuses don't survive a post-mortem.
- **Approval is a deliberate act.** Clicking merge is a decision, not a reflex. I treat it like I'd treat signing a contract.
- **Checks and balances are stacked.** Tests, scans, peer review, staged rollouts. Multiple independent ways to catch the same class of mistake.
- **Bias and fairness get explicit attention.** Especially in anything user-facing. Generated code is not neutral — it reflects what it was trained on.
- **Privacy and data handling stay in my head.** I do not paste secrets, customer data, or sensitive context into prompts. The tool is a collaborator, not a confessional.
- **I disclose where it matters.** If a process owner needs to know AI was used, they get told.

Responsible AI isn't a policy poster on the wall. It's a set of small decisions I make every hour. Done well, it's invisible. Done badly, it's the headline.

<!--
Speaker note (~2 min): This is the slide where you sound like someone who
has thought hard. Speak slowly. The room should leave knowing that the
person on stage takes accountability seriously and expects them to do the
same.
-->
