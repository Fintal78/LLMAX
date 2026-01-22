# 🟣 11. Reviews & Performance Boosters
*Description:* Adjustments based on real-world expert reviews. Technical specs don't always tell the whole story; reviews validate actual performance.
*   **Measurement:** Expert review consensus.
*   **Unit:** Multiplier (Booster)
*   **Significance:** Validates theoretical performance against real-world experience.
*   **Booster > 1.0:** Increases score (e.g., 1.05 = +5%). Used when a device outperforms its specs (e.g., great software optimization).
*   **Booster < 1.0:** Reduces score (e.g., 0.90 = -10%). Used when a device underperforms (e.g., overheating, bugs).

**Booster Methodology**
Boosters are applied strictly at the **subsection** level. This ensures that a review's specific findings impact only the relevant technical metric rather than the entire category.

### 11.A Core Principles
*   **Unaccounted Feature Requirement:** A booster is ONLY justified if it captures a characteristic or performance factor that is either entirely missing from the standard scoring system (Sections 1–10) or is significantly under-represented by the theoretical metrics.
*   **Real-World Test Exclusion (CRITICAL):** Boosters are **FORBIDDEN** for subsections that are already scored using real-world benchmarks or tests. Since these scores already reflect actual performance, applying a booster would double-count the benefit.
    *   *Excluded Subsections:* **3.1** (SoC Performance), **3.2** (CPU Efficiency), **5.1** (Battery Capacity).
*   **No Overlap:** The justification MUST NOT overlap with any existing subsection evaluations. For example, if a camera's HDR capability is already scored in Subsection 4.16, "HDR performance" cannot be used as a justification for a booster on that same subsection or any other subsection.
*   **Complete Assessment:** Before applying a booster, verify that the feature is not already scored in another section (e.g., Video Codecs vs. ISP tuning). Double-counting features is strictly prohibited.

### 11.B Justification Logic
A valid booster requires a clear logical chain linking a hidden technical feature to an observed result.
*   **Unaccounted Feature (Cause):** The specific technical mechanism, hardware component, or software algorithm that is responsible for the anomaly. This is the "Why".
*   **Unaccounted Reason (Gap):** The explicit explanation of *why* this feature is not captured by the standard scoring rules of Sections 1-10.
*   **Observed Justification (Effect):** The tangible performance outcome observed in the review. This is the "What".

### 11.C Evidence Requirements
*   **Extract Requirement:** Every justification point must be supported by an **exact, verbatim extract** from the review. This extract must be exact, meaning that searching for the extract in the review source will find it as is. **NEVER** invent, paraphrase, or hallucinate content. If the exact text is not in the source, the booster is invalid.
*   **Disjointed Extracts:** An extract may combine non-contiguous text from the same review, for example to link technical data with the resulting conclusion. Use `[...]` to indicate the separation.
*   **Content Sufficiency:** The Extract must contain enough content so that both the **Unaccounted Feature** (Cause) and the 
[!IMPORTANT]
**Observed Justification(CRITICAL)** (Effect) are directly and fully derived from it.
    *   *Formula:* `Content(Extract) ⊇ Content(Unaccounted Feature) + Content(Observed Justification)`
    This formula must be respected with outmost precision, consider the example below:
    Unaccounted Feature: 24MP Photonic Engine Output.
    Extract: "The jump from 12MP to 24MP images by default [...] made for significantly improved texture quality..."
    In this example the formula is not respected because the extract does not fully contain the unaccounted feature. Indeed, the extract only mentions the jump from 12MP to 24MP but does not mention the photonic engine output which is actually the real differentiator.
    *   *Implication:* The extract must be self-contained and explicitly link the Cause to the Effect.
*   **Technical Causality:** The extract must explicitly link the technical mechanism to the performance outcome. Purely comparative statements (e.g., "best we have seen") are **INVALID** unless they explain *why* (e.g., "thanks to the A17 Pro ISP").
*   **Proof & Precision:** The extract must contain specific quantitative data (e.g., "Delta-E 0.14", "117 points") or precise technical descriptions. Vague praise is not evidence.
*   **Source Verification:** All source links must be active, accessible URLs from reputable publications. Placeholders (e.g., `example.com`) are **STRICTLY PROHIBITED**. If a specific text extract is used, the source must be verifiable.
*   **Specificity:** Justifications must be extremely specific to the findings of the review and the technical gap they fill.
*   **Decomposition:** A single review source may impact multiple subsections; in such cases, the booster must be decomposed into separate entries.
    *   *Example:* If a review finds a phone has exceptional telephoto zoom but poor video stabilization:
        *   **Booster A (1.10):** Targets Subsection 4.5 (Zoom Capability) for superior optics.
        *   **Booster B (0.90):** Targets Subsection 4.4 (Image Stabilization) for poor software compensation.

### 11.D Process
*   **Verification Loop:** After drafting a booster, perform a mandatory self-check ensuring that **ALL** rules in sections 11.A, 11.B, and 11.C are strictly satisfied. If any rule is violated, discard and refine. Repeat this refinement process up to **3 times**. If the booster still fails to meet all criteria after the 3rd attempt, **discard the booster entirely** and log a "Verification Failed" error for that subsection.

> [!NOTE]
> The following items are **examples** of how expert reviews can be used to adjust theoretical scores. In practice, any reputable and verifiable expert review can be used as a booster source.

### 🔹 11.1 DXOMARK 24MP Texture Optimization
*   **Source Link:** [iPhone 15 Pro Max Camera Test](https://www.dxomark.com/apple-iphone-15-pro-max-camera-test/)
*   **Impacted Subsection:** 4.16 Computational Photography & AI
*   **Booster:** **1.05**
*   **Justification:**
    *   **Unaccounted Feature:** 24MP Photonic Engine Output.
    *   **Unaccounted Reason:** Section 4.3 scores the sensor's max resolution (48MP) and Section 4.16 scores HDR presence, but neither captures the computational fusion that enables a 24MP default output with superior texture rendering.
    *   **Observed Justification:** The shift to 24MP default output significantly improves texture quality.
    *   **Extract:** "The jump from 12MP to 24MP images by default [...] made for significantly improved texture quality..."

### 🔹 11.2 Tom's Guide Display Color Accuracy
*   **Source Link:** [iPhone 15 Pro Max Review](https://www.tomsguide.com/reviews/iphone-15-pro-max)
*   **Impacted Subsection:** 2.7 Color Accuracy & HDR
*   **Booster:** **1.05**
*   **Justification:**
    *   **Unaccounted Feature:** Factory Color Calibration (Delta-E 0.14).
    *   **Unaccounted Reason:** Section 2.7 scores theoretical support (DCI-P3, Dolby Vision) but does not measure the specific factory calibration accuracy (Delta-E).
    *   **Observed Justification:** The display achieves excellent color accuracy with a measured Delta-E of 0.14.
    *   **Extract:** "The iPhone 15 Pro Max’s display offers more accurate colors, as it earned a Delta-E score of 0.14..."

### 🔹 11.3 NotebookCheck PWM Flickering
*   **Source Link:** [iPhone 15 Pro Max Review](https://www.notebookcheck.net/Apple-iPhone-15-Pro-Max-review-More-camera-power-and-titanium-for-Apple-s-biggest-smartphone.756855.0.html)
*   **Impacted Subsection:** 2.1 Display Technology
*   **Booster:** **0.95**
*   **Justification:**
    *   **Unaccounted Feature:** Low-Frequency PWM Dimming (240Hz).
    *   **Unaccounted Reason:** Section 2.1 scores the OLED technology type but does not penalize low-frequency PWM dimming which can cause eyestrain for sensitive users.
    *   **Observed Justification:** Low PWM frequency causes noticeable flickering and eyestrain for sensitive users.
    *   **Extract:** "The frequency of 240 Hz is relatively low, so sensitive users will likely notice flickering..."
