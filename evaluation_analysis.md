# System Evaluation: Multi-Agent Data Science Assistant

## 1. Comparison of Runs (Titanic vs. Telecom Churn)

| Feature | Titanic Survival Analysis | Telecom Churn Analysis |
| :--- | :--- | :--- |
| **Objective** | Predict passenger survival (Binary Classification) | Predict customer churn (Binary Classification) |
| **Data Complexity** | Medium (Text, Categorical, Missing Numerical) | High (Many categorical services, contract types) |
| **Agent Performance** | High - Clear logical link between class/gender and survival. | Moderate - Churn factors are more complex; required deeper segmentation. |

## 2. Evaluation Findings

### ✅ Is the proposed plan reasonable?
**Yes.** In both cases, the **Project Planner** agent successfully translated the business objective into a standard Data Science lifecycle:
1.  **Problem Definition:** Correctly identified both as binary classification problems.
2.  **EDA Strategy:** Logic was sound (check missing values -> distributions -> correlations).
3.  **Modeling:** Proposed appropriate baselines (Logistic Regression vs. Random Forest).
*   **Strength:** The "Thinking" process of the planner is consistent and follows industry standards (CRISP-DM like approach).

### ✅ Is the EDA consistent with the dataset?
**Mostly Yes, with caveats.**
*   **Quantitative:** The **Data Analyst** correctly used the `DataStatsTool` to retrieve actual numbers (counts, means, missing values). These numbers are hard facts and were accurate.
*   **Qualitative:** The interpretation relied on the LLM. For Titanic, determining that "female" and "class 1" correlated with survival is robust. For Churn, subtle patterns (e.g., "fiber optic users churn more") might be missed if the data tool didn't explicitly capture cross-tabulations.
*   **Consistency:** The tool-use ensures the *numbers* are real, preventing pure hallucination of statistics.

### ✅ Are the proposed models plausible?
**Yes.**
*   **Titanic:** Logistic Regression and Decision Trees are the correct baselines for this simple tabular data.
*   **Churn:** Random Forest and Gradient Boosting (XGBoost) were correctly suggested as they handle mixed categorical/numerical data better than simple linear models.
*   The agents correctly identified appropriate metrics (Accuracy/F1-Score for Titanic; Recall/Precision for Churn due to class imbalance).

### ❌ Where does the Agentic AI fail? (Limitations)

1.  **Context Window & "Forgetting":**
    *   **Issue:** In complex tasks, the **Report Writer** sometimes hallucinates specific percentages if they weren't explicitly repeated in the context passed from the Analyst.
    *   **Example:** It might say "20% missing values" in the final report even if the Analyst found "22%", simply because it summarized loosely.

2.  **Lack of Iterative Refinement:**
    *   **Issue:** If the EDA reveals a surprising fact (e.g., "Total Charges" is a string, not a number), the current sequential system doesn't "go back" to fix the plan. It just pushes forward, potentially leading to errors in the modeling recommendation phase.

3.  **Code Execution vs. Recommendation:**
    *   **Limitation:** The system *recommends* code/models but doesn't *execute* the training loop. It stops at the "Proposal" stage. A true Data Science agent would try to train the model and report *actual* test accuracy.

4.  **Local LLM Constraints (Ollama/Qwen):**
    *   **Issue:** Smaller local models (like `qwen3:1.7b`) struggle with complex synthesis. They might produce repetitive text or miss logical connections that a larger model (GPT-4) would catch.

## Conclusion
The system successfully automates the **Strategic** and **Analytical** planning phases. It excels at *structuring* the problem but relies on the human user to execute the final modeling code. It is a "Co-pilot" rather than an "Auto-pilot".
