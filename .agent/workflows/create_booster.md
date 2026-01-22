---
description: How to create and verify a new Performance Booster in scoring_rules.md
---

# Booster Creation & Verification Workflow

This workflow enforces the strict rules defined in Section 11 of `scoring_rules.md`. You MUST follow this process for every single booster you create.

## 1. Eligibility Check (Rule 11.A)
- [ ] **Identify the Unaccounted Feature:** What specific technical feature is missing from the standard scoring?
- [ ] **Check Exclusion List:** Is the impacted subsection 3.1, 3.2, or 5.1? If YES, STOP. Booster is forbidden.
- [ ] **Check Overlap:** Is this feature already scored in another section? (e.g. Codecs in 4.11). If YES, STOP.

## 2. Source Selection (Rule 11.C)
- [ ] **Find a Reputable Source:** Search for a review from a known publication (GSMArena, AnandTech, DXOMARK, etc.).
- [ ] **Find the Extract:** Locate a specific, verbatim sentence that links the Feature (Cause) to the Performance (Effect).
- [ ] **Capture the URL:** Get the exact permalink to the review page.

## 3. Functional Verification (Rule 11.C - CRITICAL)
- [ ] **Run `read_url_content(Url=...)`:** You MUST execute this tool on the URL.
- [ ] **Verify Status:** Did the tool return a success (200 OK) and content?
- [ ] **Verify Content:** Does the `Extract` text exist verbatim in the tool output?
    - *If NO:* The source is invalid or the extract is hallucinated. FIND A NEW SOURCE.

## 4. Draft the Booster (Rule 11.B)
- [ ] **Format:**
    ```markdown
    ### 🔹 11.x [Source Name] [Topic]
    *   **Source Link:** [Title](URL)
    *   **Impacted Subsection:** [X.Y Name]
    *   **Booster:** [Value]
    *   **Justification:**
        *   **Unaccounted Feature:** [Technical Cause]
        *   **Unaccounted Reason:** [Why it's not scored]
        *   **Observed Justification:** [Performance Effect]
        *   **Extract:** "[Verbatim Quote]"
    ```

## 5. Final Review (Rule 11.D)
- [ ] **Content Sufficiency:** Does Extract contain BOTH Cause and Effect?
- [ ] **Technical Causality:** Is it causal ("because of X") and not just comparative ("better than Y")?
- [ ] **Proof:** Does it have data or specific technical terms?

// turbo
6. Update `scoring_rules.md` only if all checks pass.
