# Quick Start Guide

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file in the project root:

```bash
# Copy the example file
copy .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-key-here
```

### 3. Generate Sample Datasets (Optional)

```bash
# Generate Titanic dataset
python datasets/generate_titanic.py

# Generate customer churn dataset
python datasets/generate_churn.py
```

## Usage Examples

### Example 1: Titanic Survival Analysis

```bash
python main.py \
  --topic "Predict passenger survival on the Titanic based on demographics and ticket information" \
  --csv "datasets/titanic_sample.csv" \
  --output "titanic_report.md"
```

### Example 2: Customer Churn Prediction

```bash
python main.py \
  --topic "Identify customers likely to churn from a telecommunications company" \
  --csv "datasets/telecom_churn_sample.csv" \
  --output "churn_report.md"
```

### Example 3: Custom Dataset

```bash
python main.py \
  --topic "Your business objective here" \
  --csv "path/to/your/dataset.csv" \
  --output "custom_report.md"
```

## Command Line Arguments

| Argument | Required | Description | Default |
|----------|----------|-------------|---------|
| `--topic` | Yes | Business description or analysis objective | - |
| `--csv` | Yes | Path to CSV dataset file | - |
| `--output` | No | Output filename for final report | `report_final.md` |

## What Happens During Execution

The system executes 4 sequential tasks:

1. **Planning (Project Planner Agent)**
   - Analyzes business objective
   - Creates detailed work plan
   - Defines success criteria
   - Output: Work plan document

2. **Analysis (Data Analyst Agent)**
   - Reads dataset using CSVReaderTool
   - Computes statistics using DataStatsTool
   - Identifies patterns and quality issues
   - Output: Comprehensive EDA report

3. **Modeling (Modeling Agent)**
   - Determines problem type
   - Recommends 2-3 baseline models
   - Defines evaluation metrics
   - Output: Model recommendations

4. **Report Writing (Report Writer Agent)**
   - Synthesizes all findings
   - Creates professional technical report
   - Includes executive summary and recommendations
   - Output: Final technical report (Markdown)

## Expected Execution Time

- Small datasets (<10K rows): 3-5 minutes
- Medium datasets (10K-100K rows): 5-8 minutes
- Large datasets (>100K rows): 8-15 minutes

*Note: Time depends on dataset complexity and API response times*

## Output Structure

The final report will include:

```markdown
# Executive Summary
Brief overview of objectives, approach, and key findings

# 1. Introduction
Business context, dataset description, analysis approach

# 2. Exploratory Data Analysis
Dataset statistics, data quality, patterns, feature analysis

# 3. Baseline Models and Evaluation
Problem formulation, proposed models, evaluation metrics

# 4. Discussion and Insights
Key findings, modeling implications, limitations

# 5. Conclusions and Recommendations
Summary and actionable next steps
```

## Troubleshooting

### Error: "OPENAI_API_KEY not found"
- Ensure you have created a `.env` file
- Verify your API key is correct
- Check that `.env` is in the project root directory

### Error: "CSV file not found"
- Verify the path to your CSV file is correct
- Use absolute paths or paths relative to project root
- Generate sample datasets if testing

### Error: "Module not found"
- Run `pip install -r requirements.txt`
- Ensure you're in the correct virtual environment

### Execution hangs or is very slow
- Check your internet connection
- Verify OpenAI API status
- Ensure you have sufficient API credits
- Some datasets may require more processing time

## Tips for Best Results

1. **Clear Business Objectives**: Provide specific, detailed topic descriptions
2. **Clean Data**: Well-formatted CSV files produce better results
3. **Column Names**: Use descriptive column names
4. **Dataset Size**: System works best with 100-100K rows
5. **Problem Clarity**: Clearly state if it's classification, regression, etc.

## Next Steps After Getting Results

1. Review the generated technical report
2. Validate EDA findings against actual dataset
3. Assess appropriateness of proposed models
4. Use evaluation.md template to document findings
5. Implement recommended baseline models
6. Iterate with different datasets or business objectives
