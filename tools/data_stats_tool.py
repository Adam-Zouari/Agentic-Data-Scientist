"""DataStatsTool - Computes statistical summaries for datasets."""
from crewai.tools import tool
import pandas as pd
import numpy as np
import os


@tool("Data Statistics")
def data_stats_tool(csv_path: str) -> str:
    """
    Computes comprehensive statistical summaries for a dataset.
    Provides descriptive statistics (mean, median, std, min, max) for numerical columns,
    cardinality and frequency analysis for categorical columns,
    missing value percentages, and distribution insights.
    Use this tool to perform exploratory data analysis.
    
    Args:
        csv_path: Path to the CSV file to analyze
    
    Returns:
        String containing statistical analysis
    """
    try:
        # Check if file exists
        if not os.path.exists(csv_path):
            return f"Error: File not found at path: {csv_path}"
        
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Prepare output
        output = []
        output.append("=" * 80)
        output.append("STATISTICAL ANALYSIS")
        output.append("=" * 80)
        output.append(f"\nDataset: {csv_path}")
        output.append(f"Total Records: {len(df):,}")
        output.append(f"Total Features: {len(df.columns)}")
        
        # Identify column types
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        
        output.append(f"\nNumeric Columns: {len(numeric_cols)}")
        output.append(f"Categorical Columns: {len(categorical_cols)}")
        
        # Numerical statistics
        if numeric_cols:
            output.append("\n" + "=" * 80)
            output.append("NUMERICAL FEATURES STATISTICS")
            output.append("=" * 80)
            
            for col in numeric_cols:
                output.append(f"\n{col}:")
                output.append(f"  Mean: {df[col].mean():.4f}")
                output.append(f"  Median: {df[col].median():.4f}")
                output.append(f"  Std Dev: {df[col].std():.4f}")
                output.append(f"  Min: {df[col].min():.4f}")
                output.append(f"  Max: {df[col].max():.4f}")
                output.append(f"  25th Percentile: {df[col].quantile(0.25):.4f}")
                output.append(f"  75th Percentile: {df[col].quantile(0.75):.4f}")
                
                missing_pct = (df[col].isnull().sum() / len(df)) * 100
                if missing_pct > 0:
                    output.append(f"  Missing Values: {df[col].isnull().sum()} ({missing_pct:.2f}%)")
                
                # Detect potential outliers (IQR method)
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                outliers = ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()
                if outliers > 0:
                    output.append(f"  Potential Outliers: {outliers} ({(outliers/len(df)*100):.2f}%)")
        
        # Categorical statistics
        if categorical_cols:
            output.append("\n" + "=" * 80)
            output.append("CATEGORICAL FEATURES STATISTICS")
            output.append("=" * 80)
            
            for col in categorical_cols:
                output.append(f"\n{col}:")
                output.append(f"  Cardinality: {df[col].nunique()} unique values")
                
                missing_pct = (df[col].isnull().sum() / len(df)) * 100
                if missing_pct > 0:
                    output.append(f"  Missing Values: {df[col].isnull().sum()} ({missing_pct:.2f}%)")
                
                # Top categories
                value_counts = df[col].value_counts()
                output.append(f"  Top 5 Categories:")
                for idx, (val, count) in enumerate(value_counts.head(5).items(), 1):
                    pct = (count / len(df)) * 100
                    output.append(f"    {idx}. {val}: {count} ({pct:.2f}%)")
                
                # Check for high cardinality
                if df[col].nunique() > len(df) * 0.5:
                    output.append(f"  ⚠️  High cardinality detected (may be an ID or unique identifier)")
        
        # Overall missing value summary
        output.append("\n" + "=" * 80)
        output.append("MISSING VALUES SUMMARY")
        output.append("=" * 80)
        total_missing = df.isnull().sum().sum()
        total_cells = df.shape[0] * df.shape[1]
        output.append(f"\nTotal Missing Values: {total_missing:,} ({(total_missing/total_cells*100):.2f}% of all data)")
        
        missing_by_col = df.isnull().sum()
        if missing_by_col.sum() > 0:
            output.append("\nColumns with Missing Values:")
            for col in missing_by_col[missing_by_col > 0].sort_values(ascending=False).index:
                pct = (missing_by_col[col] / len(df)) * 100
                output.append(f"  {col}: {missing_by_col[col]:,} ({pct:.2f}%)")
        else:
            output.append("\n✓ No missing values in any column")
        
        # Data quality insights
        output.append("\n" + "=" * 80)
        output.append("DATA QUALITY INSIGHTS")
        output.append("=" * 80)
        
        insights = []
        
        # Check for duplicates
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            insights.append(f"⚠️  Found {duplicates} duplicate rows ({(duplicates/len(df)*100):.2f}%)")
        else:
            insights.append("✓ No duplicate rows detected")
        
        # Check for constant columns
        constant_cols = [col for col in df.columns if df[col].nunique() == 1]
        if constant_cols:
            insights.append(f"⚠️  Constant columns (single value): {', '.join(constant_cols)}")
        
        # Check for high missing percentage columns
        high_missing = [col for col in df.columns if (df[col].isnull().sum() / len(df)) > 0.5]
        if high_missing:
            insights.append(f"⚠️  Columns with >50% missing values: {', '.join(high_missing)}")
        
        if insights:
            for insight in insights:
                output.append(f"\n{insight}")
        
        output.append("\n" + "=" * 80)
        
        return "\n".join(output)
        
    except Exception as e:
        return f"Error computing statistics: {str(e)}"
