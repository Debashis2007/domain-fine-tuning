# Design: Domain Fine-Tuning

**Project:** `domain-fine-tuning`  
**Parent system design:** [08 — Fine-Tuning / Eval Data Pipelines](https://github.com/Debashis2007/domain-fine-tuning/blob/main/08-finetuning-eval-data-pipelines.md)

## 1. What this POC demonstrates

Train entrypoint refuses anything except registry-blessed dataset URIs with lineage metadata.

## 2. Architecture (POC)

```text
POST /train → registry lookup → start artifact
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Blessed registry gate | Poison/unapproved data must not train. | 404/400 if missing. |
| Lineage stub | Checkpoint must map to data hash. | `lineage` object. |
| Domain tag | Vertical FT tracking. | `domain` in registry. |

## 4. Key endpoints

`GET /health`, `POST /train`

## 5. Tradeoffs / POC limits

No actual trainer process — gate only.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

> **Watch on YouTube:** [Domain Fine Tuning — System Design #Shorts](https://youtu.be/nrosR3ZN65k)
>
> Direct link: **https://youtu.be/nrosR3ZN65k**

Also available in-repo:
- GIF preview: [`video/design-overview.gif`](./video/design-overview.gif)
- MP4 download: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Narration script: [`video/narration.txt`](./video/narration.txt)

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

