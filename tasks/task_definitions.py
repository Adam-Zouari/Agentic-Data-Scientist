"""Task definitions for the multi-agent data science crew."""
from crewai import Task
from typing import List


def create_tasks(planner, analyst, modeler, writer, topic: str, csv_path: str) -> List[Task]:
    """
    Create all tasks for the data science crew.
    
    Args:
        planner: Project Planner Agent
        analyst: Data Analyst Agent
        modeler: Modeling Agent
        writer: Report Writer Agent
        topic: Business description/analysis objective
        csv_path: Path to the CSV dataset
        
    Returns:
        List of Task objects in execution order
    """
    
    # Task 1: Planning
    planning_task = Task(
        description=(
            f"Based on the business objective: '{topic}', create a comprehensive "
            f"data science work plan. Your plan should include:\n"
            f"1. Problem definition and business context\n"
            f"2. Key questions to answer through analysis\n"
            f"3. Detailed steps for exploratory data analysis (EDA)\n"
            f"4. Considerations for data quality and preprocessing\n"
            f"5. Potential modeling approaches to consider\n"
            f"6. Success criteria and evaluation approach\n"
            f"7. Timeline and milestones\n\n"
            f"The plan should be actionable and guide the entire analysis process. "
            f"Consider the dataset located at: {csv_path}\n\n"
            f"Be thorough but concise. Focus on what's important for this specific project."
        ),
        expected_output=(
            "A detailed, structured work plan document (500-800 words) organized with clear sections:\n"
            "- Project Overview and Objectives\n"
            "- Key Business Questions\n"
            "- Exploratory Data Analysis Steps\n"
            "- Data Quality Considerations\n"
            "- Modeling Strategy\n"
            "- Evaluation Criteria\n"
            "- Project Timeline\n\n"
            "The plan should be specific to the business objective and provide clear guidance "
            "for subsequent analysis and modeling tasks."
        ),
        agent=planner
    )
    
    # Task 2: Exploratory Data Analysis
    analysis_task = Task(
        description=(
            f"Perform comprehensive exploratory data analysis on the dataset at: {csv_path}\n\n"
            f"Follow the work plan from the Project Planner. Use your tools to:\n"
            f"1. Read and understand the dataset structure (columns, data types, shape)\n"
            f"2. Compute detailed statistical summaries for all features\n"
            f"3. Identify data quality issues (missing values, outliers, duplicates)\n"
            f"4. Analyze distributions of key variables\n"
            f"5. Identify potential relationships and patterns\n"
            f"6. Highlight important features for modeling\n\n"
            f"Your analysis should be thorough and data-driven, using the CSV Reader "
            f"and Data Statistics tools to extract insights. Focus on findings that are "
            f"relevant to the business objective: {topic}\n\n"
            f"Provide both statistical rigor and practical insights."
        ),
        expected_output=(
            "A comprehensive EDA report (800-1200 words) structured as:\n"
            "- Dataset Overview (shape, features, types)\n"
            "- Statistical Summary (descriptive statistics for all features)\n"
            "- Data Quality Assessment (missing values, outliers, anomalies)\n"
            "- Distribution Analysis (key patterns and characteristics)\n"
            "- Feature Insights (important variables and relationships)\n"
            "- Recommendations for preprocessing and modeling\n\n"
            "The report should be detailed, data-driven, and include specific numbers "
            "and percentages from the actual dataset analysis."
        ),
        agent=analyst,
        context=[planning_task]
    )
    
    # Task 3: Model Recommendation
    modeling_task = Task(
        description=(
            f"Based on the business objective '{topic}' and the EDA findings, propose "
            f"2-3 appropriate baseline machine learning models.\n\n"
            f"Your recommendations should:\n"
            f"1. Identify the problem type (classification, regression, clustering, etc.)\n"
            f"2. Propose 2-3 suitable baseline models with clear rationale\n"
            f"3. Explain why each model is appropriate for this specific problem\n"
            f"4. Define comprehensive evaluation metrics for the problem type\n"
            f"5. Discuss expected model performance and limitations\n"
            f"6. Provide implementation considerations\n\n"
            f"Focus on simple, interpretable baseline models that can be implemented quickly "
            f"and serve as benchmarks. Consider the data characteristics revealed in the EDA."
        ),
        expected_output=(
            "A structured modeling recommendation document (600-900 words) containing:\n"
            "- Problem Type Classification (with justification)\n"
            "- Baseline Model Recommendations (2-3 models):\n"
            "  * Model name and type\n"
            "  * Why it's appropriate for this problem\n"
            "  * Key hyperparameters to consider\n"
            "  * Strengths and limitations\n"
            "- Evaluation Metrics:\n"
            "  * Primary metrics (with definitions)\n"
            "  * Secondary metrics\n"
            "  * Rationale for metric selection\n"
            "- Implementation Considerations\n"
            "- Expected Performance Range\n\n"
            "Provide clear, actionable recommendations grounded in ML best practices."
        ),
        agent=modeler,
        context=[planning_task, analysis_task]
    )
    
    # Task 4: Report Writing
    report_task = Task(
        description=(
            f"Compile all findings into a comprehensive, professional technical report.\n\n"
            f"Synthesize the work plan, EDA findings, and modeling recommendations into "
            f"a cohesive narrative. The report should:\n"
            f"1. Start with an executive summary\n"
            f"2. Provide clear introduction with business context\n"
            f"3. Present EDA findings in an organized, accessible manner\n"
            f"4. Explain proposed models and evaluation approach\n"
            f"5. Include discussion of key insights and implications\n"
            f"6. Conclude with actionable recommendations\n\n"
            f"Business objective: {topic}\n"
            f"Dataset: {csv_path}\n\n"
            f"Use proper Markdown formatting with clear headings, bullet points, "
            f"and logical flow. Make the report accessible to both technical and "
            f"business audiences. Ensure all sections are well-connected and tell "
            f"a coherent story from problem to solution."
        ),
        expected_output=(
            "A complete, well-formatted technical report in Markdown (1500-2500 words) with:\n\n"
            "# Executive Summary\n"
            "- Brief overview of objectives, approach, and key findings (150-200 words)\n\n"
            "# 1. Introduction\n"
            "- Business context and objectives\n"
            "- Dataset description\n"
            "- Analysis approach\n\n"
            "# 2. Exploratory Data Analysis\n"
            "- Dataset overview and statistics\n"
            "- Data quality assessment\n"
            "- Key patterns and insights\n"
            "- Feature analysis\n\n"
            "# 3. Baseline Models and Evaluation\n"
            "- Problem formulation\n"
            "- Proposed baseline models (2-3)\n"
            "- Evaluation metrics and rationale\n"
            "- Implementation considerations\n\n"
            "# 4. Discussion and Insights\n"
            "- Key findings from analysis\n"
            "- Modeling implications\n"
            "- Limitations and challenges\n\n"
            "# 5. Conclusions and Recommendations\n"
            "- Summary of main findings\n"
            "- Actionable next steps\n"
            "- Expected business impact\n\n"
            "The report should be professional, well-organized, and ready for stakeholder review."
        ),
        agent=writer,
        context=[planning_task, analysis_task, modeling_task]
    )
    
    return [planning_task, analysis_task, modeling_task, report_task]
