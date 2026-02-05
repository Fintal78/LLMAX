# Verification Log Template

**Target Subsection:** [Subsection Name and Number]  
**Source:** [Title]([URL])
**Verification Iterations:** [Number of loops executed before passing]

## 1. Rule 11.A: Core Principles
- [ ] **Unaccounted Feature Requirement:** [Explain why the feature is missing from standard scoring (Sections 1-10)]
- [ ] **Real-World Test Exclusion:** [Confirm impacted subsection is NOT 3.1, 3.2, or 5.1]
- [ ] **No Overlap:** [Confirm no overlap with other specific sections (e.g., Display vs Camera)]
- [ ] **Complete Assessment:** [Confirm feature is strictly specific to this subsection and not double-counted]

## 2. Rule 11.B: Justification Logic
- [ ] **Source Link:** [Valid, accessible public URL?]
- [ ] **Impacted Subsection:** [Correct subsection number?]
- [ ] **Booster:** [Value > 1.0 for bonus, < 1.0 for malus]
- [ ] **Justification Chain:**
    - **Cause (Unaccounted Feature):** "[Paste verbatim extract explaining the technical mechanism/cause]"
    - **Gap (Unaccounted Reason):** [Explanation of the gap]
    - **Effect (Observed Justification):** "[Paste verbatim extract dealing with the observed result]"
- [ ] **Extract Requirement:** [Are both extracts EXACT verbatim copies from the source?]
- [ ] **Technical Causality:** [Does the Cause strictly lead to the Effect? No vague "better because better" logic]

## 3. Rule 11.C: Evidence Requirements
- [ ] **Proof & Precision:** [Do extracts contain quantitative data or precise technical terms?]
- [ ] **Source Verification:** [Is the source reputable and verifiable?]
- [ ] **Specificity:** [Is the justification specific to the exact technical gap?]
- [ ] **Decomposition:** [If the review mentions multiple issues, is this booster focused on just ONE of them?]

## 4. Rule 11.D: Conclusion
- [ ] **Verification Status:** **PASS** / **FAIL**
- [ ] **Action:** [Commit (if PASS) / Discard (if FAIL)]
