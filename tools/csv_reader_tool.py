"""CSVReaderTool - Reads and previews CSV files."""
from crewai.tools import tool
import pandas as pd
import os


@tool("CSV Reader")
def csv_reader_tool(csv_path: str, num_rows: int = 5) -> str:
    """
    Reads a CSV file and provides information about its structure.
    Returns column names, data types, dataset shape, sample rows,
    and identifies columns with missing values.
    Use this tool to understand the structure of the dataset.
    
    Args:
        csv_path: Path to the CSV file to read
        num_rows: Number of sample rows to display (default: 5)
    
    Returns:
        String containing CSV file information
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
        output.append("CSV FILE INFORMATION")
        output.append("=" * 80)
        output.append(f"\nFile Path: {csv_path}")
        output.append(f"Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        
        # Column information
        output.append("\n" + "-" * 80)
        output.append("COLUMN INFORMATION")
        output.append("-" * 80)
        output.append(f"\nTotal Columns: {len(df.columns)}")
        output.append("\nColumn Names and Data Types:")
        for idx, (col, dtype) in enumerate(zip(df.columns, df.dtypes), 1):
            output.append(f"  {idx}. {col} ({dtype})")
        
        # Missing values
        missing = df.isnull().sum()
        if missing.sum() > 0:
            output.append("\n" + "-" * 80)
            output.append("MISSING VALUES")
            output.append("-" * 80)
            for col in missing[missing > 0].index:
                pct = (missing[col] / len(df)) * 100
                output.append(f"  {col}: {missing[col]} ({pct:.2f}%)")
        else:
            output.append("\nNo missing values detected.")
        
        # Sample rows
        output.append("\n" + "-" * 80)
        output.append(f"SAMPLE DATA (First {num_rows} rows)")
        output.append("-" * 80)
        output.append("\n" + df.head(num_rows).to_string())
        
        output.append("\n" + "=" * 80)
        
        return "\n".join(output)
        
    except Exception as e:
        return f"Error reading CSV file: {str(e)}"
