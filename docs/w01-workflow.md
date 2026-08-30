# W01 Workflow

## Workflow Diagram

```mermaid
flowchart LR
    A[Learner] --> B[Coursera / Git Lab]
    B --> C[Tests]
    C --> D[Evidence Report]
    D --> E[Sprint Gate]

Connection Explanations
1. Learner → Coursera / Git Lab
   The learner studies Git concepts and demonstrates them through practical exercises and labs.
2. Coursera / Git Lab → Tests
   Practical work is verified using tests, repository inspection, Git status, diffs, and history checks.
3. Tests → Evidence Report
   Verified outputs, commit hashes, Git graphs, screenshots, and results are recorded as evidence.
4. Evidence Report → Sprint Gate
   The completed evidence is reviewed against the W01 acceptance criteria before the sprint can be closed.
W01 Gate Logic
LEARN
  ↓
PRACTICE
  ↓
TEST
  ↓
CAPTURE EVIDENCE
  ↓
VERIFY
  ↓
CLOSE W01
