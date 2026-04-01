---
name: research-ops
description: Evidence-first research workflow for Hermes. Use when answering current questions, evaluating a market or tool, enriching leads, comparing strategic options, or deciding whether a request should become ongoing monitored data collection.
metadata:
  hermes:
    tags: [generated, research, market, discovery, monitoring, workflow, verification]
---

# Research Ops

Use this when the user asks Hermes to research something current, compare options, enrich people or companies, or turn repeated lookups into an ongoing monitoring workflow.

## Skill Stack

Pull these imported skills into the workflow when relevant:
- `deep-research` for multi-source cited synthesis
- `market-research` for decision-oriented framing
- `exa-search` for first-pass discovery and current-web retrieval
- `continuous-agent-loop` when the task spans user-provided evidence, fresh verification, and a final recommendation across multiple turns
- `data-scraper-agent` when the user really needs recurring collection or monitoring
- `search-first` before building new scraping or enrichment logic
- `eval-harness` mindset for claim quality, freshness, and explicit uncertainty

## When To Use

- user says `research`, `look up`, `find`, `who should i talk to`, `what's the latest`, or similar
- the answer depends on current public information, external sources, or a ranked set of candidates
- the user pastes a compaction summary, copied research, manual calculations, or says `factor this in`
- the user asks `should i do X or Y`, `compare these options`, or wants an explicit recommendation under uncertainty
- the task sounds recurring enough that a scraper or scheduled monitor may be better than a one-off search

## Workflow

1. Start from the evidence already in the prompt:
   - treat compaction summaries, pasted research, copied calculations, and quoted assumptions as loaded inputs
   - normalize them into `user-provided evidence`, `needs verification`, and `open questions`
   - do not restart the analysis from zero if the user already gave you a partial model
2. Classify the ask before searching:
   - quick factual answer
   - decision memo or comparison
   - lead list or enrichment
   - recurring monitoring request
3. Build the decision surface before broad searching when the ask is comparative:
   - list the options, decision criteria, constraints, and assumptions explicitly
   - keep concrete numbers and dates attached to the option they belong to
   - mark which variables are already evidenced and which still need outside verification
4. Start with the fastest evidence path:
   - use `exa-search` first for broad current-web discovery
   - if the question is about a local wrapper, config, or checked-in code path, inspect the live local source before making any web claim
5. Deepen only where the evidence justifies it:
   - use `deep-research` when the user needs synthesis, citations, or multiple angles
   - use `market-research` when the result should end in a recommendation, ranking, or go/no-go call
   - keep `continuous-agent-loop` discipline when the task spans user evidence, fresh searches, and recommendation updates across interruptions
6. Separate fact from inference:
   - label sourced facts clearly
   - label user-provided evidence clearly
   - label inferred fit, ranking, or recommendation as inference
   - include dates when freshness matters
7. Decide whether this should stay manual:
   - if the user will likely ask for the same scan repeatedly, use `data-scraper-agent` patterns or propose a monitored collection path instead of repeating the same manual research forever
8. Report with evidence:
   - group the answer into sourced facts, user-provided evidence, inference, and recommendation when the ask is a comparison or decision
   - cite the source or local file behind each important claim
   - if evidence is thin or conflicting, say so directly

## Pitfalls

- do not answer current questions from stale memory when a fresh search is cheap
- do not conflate local code-backed behavior with market or web evidence
- do not ignore pasted research or compaction context and redo the whole investigation from scratch
- do not mix user-provided assumptions into sourced facts without labeling them
- do not present unsourced numbers or rankings as facts
- do not spin up a heavy deep-research pass for a quick capability check that local code can answer
- do not leave the comparison criteria implicit when the user asked for a recommendation
- do not keep one-off researching a repeated monitoring ask when automation is the better fit

## Verification

- important claims have a source, file path, or explicit inference label
- user-provided evidence is surfaced as a distinct layer when it materially affects the answer
- freshness-sensitive answers include concrete dates when relevant
- recurring-monitoring recommendations state whether the task should remain manual or graduate to a scraper/workflow
