# Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.
# Unauthorized copying, modification, or distribution is prohibited.
# https://github.com/Debashis2007

"""Domain Fine-Tuning — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "Domain Fine-Tuning"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(USE_CASE)


registry = {"blessed@legal-v1": {"hash": "sha256:abc", "domain": "legal"}}

class TrainIn(BaseModel):
    dataset: str

@app.post("/train")
def train(body: TrainIn):
    meta = registry.get(body.dataset)
    if not meta:
        raise HTTPException(400, detail="refusing unblessed dataset URI")
    return {"started": True, "dataset": body.dataset, "lineage": meta, "artifact": "ft-legal-001"}
