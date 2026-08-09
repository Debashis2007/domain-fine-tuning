# Use Case: Domain Fine-Tuning

**YouTube walkthrough:** [Domain Fine Tuning — System Design #Shorts](https://youtu.be/nrosR3ZN65k)

**Design doc:** [docs/DESIGN.md](./docs/DESIGN.md) — architecture, patterns, and why.


**Parent system design:** [08 — Fine-Tuning / Eval Data Pipelines](../08-finetuning-eval-data-pipelines.md)  
**Also references:** [03 — Training orchestration](../03-distributed-training-orchestration.md)

## Users & problem

A vertical product (legal, medical, code) needs a domain-adapted model. Training must use only blessed domain data with full lineage.

## Requirements & SLOs

| Requirement | Target |
|-------------|--------|
| Inputs | Blessed dataset@version only |
| Lineage | Checkpoint → data → code pins |
| Eval | Domain suite + leakage firewall |
| Promote | Gate before serving |

## Design (from parent)

```
Domain corpora → validate/quarantine → blessed manifest
  → train job ([03](../03-distributed-training-orchestration.md))
  → domain evals → registry artifact
  → canary ([05](../05-model-monitoring-observability.md))
```

## Specializations

| Concern | Domain FT choice |
|---------|------------------|
| Experts | SME review sampling |
| Risk | Higher bar for regulated domains |
| Mix | Blend general + domain to avoid collapse |
| Privacy | Customer data isolation / ZDR |

## Failure modes

- Unblessed spreadsheet sneaks in → train job refuses non-registry URIs.
- Eval leakage → firewall at publish.
- Catastrophic forgetting → keep general eval suite in gate.




## Design walkthrough (opens on GitHub)

> **Watch on YouTube:** [Domain Fine Tuning — System Design #Shorts](https://youtu.be/nrosR3ZN65k)


![Design overview](docs/video/design-overview.gif)

Full narrated video (download): [docs/video/design-overview.mp4](docs/video/design-overview.mp4)

## Run (self-contained POC)

This folder is a **standalone** project (safe to split into its own GitHub repo).

```bash
cd domain-fine-tuning
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.main:app --reload --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health | jq
```

curl -s -X POST http://127.0.0.1:8000/train -H 'Content-Type: application/json' -d '{"dataset":"blessed@legal-v1"}' | jq

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

