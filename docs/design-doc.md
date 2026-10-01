# PayFlow: Design Doc

**Author:** Salman Shaikh  ·  **Status:** Draft  ·  **Last updated:** 2026-10-01

## 1. Problem
<!-- What problem do businesses have that PayFlow solves?
     Who are the users? (Hint: two kinds—merchants and their customers.)
     Why is this hard? (Think: money, retries, failures.) -->

## 2. Goals
<!-- 3–5 bullets. What MUST PayFlow do? Be specific and testable.
     Bad: "Payments should work well."
     Good: "A merchant can create, capture, and refund a payment via REST API." -->

## 3. Non-goals
<!-- 3–5 bullets. What are we deliberately NOT building, and why?
     (Hint: real banks? real card networks? a mobile app? compliance?) -->

## 4. Requirements
<!-- Split into:
     Functional (what it does) — e.g. create/retrieve/list customers.
     Non-functional (how well) — correctness, availability, latency, security.
     For each non-functional one: how will we PROVE it? (a test? a load test?) -->

## 5. High-level design
<!-- Today's architecture in a small ASCII diagram, e.g.
     Client ──HTTP──▶ FastAPI app ──▶ (in-memory dict, later Postgres)
     Then: what is in the codebase now (app/, tests/, CI) and where it's heading
     (milestones M1–M3 in one line each). -->

## 6. Risks & open questions
<!-- What could go wrong with this PROJECT? (scope creep, time, complexity)
     What don't you know yet? (e.g. "How do we prevent double charges?") -->