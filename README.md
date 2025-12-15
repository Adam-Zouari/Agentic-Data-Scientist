# Multi-Agent Agentic AI System for Data Science

A sophisticated multi-agent system built with CrewAI that assists data scientists in analyzing datasets and generating comprehensive technical reports.

## Overview

This system uses 4 specialized AI agents that collaborate to:
- Create detailed analysis plans from business descriptions
- Perform exploratory data analysis (EDA)
- Propose baseline machine learning models
- Generate professional technical reports

## Architecture

The system consists of:

1. **Project Planner Agent**: Translates business requirements into actionable work plans
2. **Data Analyst Agent**: Performs comprehensive EDA using custom tools
3. **Modeling Agent**: Proposes baseline models and evaluation metrics
4. **Report Writer Agent**: Compiles findings into coherent technical reports

## Installation

```bash
# Clone the repository
cd AgenticAI

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create a .env file with:
# OPENAI_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

```bash
python main.py --topic "Customer churn prediction" --csv "path/to/dataset.csv"
```

### Arguments

- `--topic`: Business description or analysis objective (required)
- `--csv`: Path to CSV dataset file (required)
- `--output`: Output report filename (default: report_final.md)

### Example

```bash
python main.py \
  --topic "Predict customer churn for a telecommunications company" \
  --csv "datasets/telecom_churn.csv" \
  --output "telecom_analysis.md"
```

## Project Structure

```
AgenticAI/
├── agents/              # Agent definitions
│   ├── planner_agent.py
│   ├── data_analyst_agent.py
│   ├── modeling_agent.py
│   └── report_writer_agent.py
├── tasks/               # Task definitions
│   └── task_definitions.py
├── tools/               # Custom tools
│   ├── csv_reader_tool.py
│   └── data_stats_tool.py
├── docs/                # Documentation
│   ├── architecture.md
│   └── evaluation.md
├── datasets/            # Sample datasets
├── main.py              # Main execution script
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Custom Tools

- **CSVReaderTool**: Reads CSV files, displays schema and sample data
- **DataStatsTool**: Computes statistical summaries and data quality metrics

## Output

The system generates a structured technical report containing:

1. **Introduction**: Business context and objectives
2. **Exploratory Data Analysis**: Statistical summaries, distributions, insights
3. **Baseline Models**: Proposed models with rationale
4. **Evaluation Metrics**: Appropriate metrics for the problem type
5. **Discussion and Conclusions**: Key findings and recommendations

## Requirements

- Python 3.8+
- OpenAI API key
- Pandas-compatible CSV dataset

## License

MIT License
