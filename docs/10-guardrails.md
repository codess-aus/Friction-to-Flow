![Guardrails](assets/10-guardrails.png){ .hero }

# Chapter 10 — Guardrails

> *Speed without oversight is just a faster way to ship a problem.*

If you take an amplifier and point it at a process with no guardrails, you don't get more good outcomes — you get more outcomes, full stop. Some of them will be excellent. Some of them will be expensive mistakes shipped at speed.

So I am uncompromising about the guardrails I keep around this workflow:

- **I review every line.** Every diff. Every PR. Whether a human wrote it or an agent did. *Read it* — don't skim. If I can't explain what a line does, it doesn't get merged.
- **Tests are not optional.** Generated tests are still tests. They need to be meaningful, not decorative. I read them like a reviewer, not a beneficiary.
- **Security checks are continuous, not ceremonial.** Code scanning, secret scanning, dependency review — they live in the pipeline and they block. I don't argue with a true positive because it slows me down.
- **Small PRs.** The agent's speed is no excuse to land a 4,000-line change nobody can review. Keep the units of change reviewable.
- **Reproducibility.** I want to be able to explain *why* a change exists. The prompt, the plan, the diff — all of it part of the record.
- **Rollback is cheap and rehearsed.** Speed forward requires a credible way back.

The guardrails are not a tax on speed. They're the reason speed is safe enough to keep. Without them, the same tool that gave me flow gives me incidents.

<!--
Speaker note (~2 min): Hit this firmly. You are the adult in the room here.
If the audience hears "guardrails are friction," they have misunderstood.
Guardrails are what makes the speed *sustainable*.
-->
