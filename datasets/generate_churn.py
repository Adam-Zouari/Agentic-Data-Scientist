"""
Generate a sample customer churn dataset for testing the multi-agent system.
This simulates a telecommunications company customer database.
"""
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(123)

# Create sample customer churn dataset
n_samples = 7043

data = {
    'customerID': [f'CUST-{i:05d}' for i in range(1, n_samples + 1)],
    'gender': np.random.choice(['Male', 'Female'], n_samples),
    'SeniorCitizen': np.random.choice([0, 1], n_samples, p=[0.84, 0.16]),
    'Partner': np.random.choice(['Yes', 'No'], n_samples, p=[0.52, 0.48]),
    'Dependents': np.random.choice(['Yes', 'No'], n_samples, p=[0.30, 0.70]),
    'tenure': np.random.randint(0, 73, n_samples),
    'PhoneService': np.random.choice(['Yes', 'No'], n_samples, p=[0.90, 0.10]),
    'MultipleLines': np.random.choice(['Yes', 'No', 'No phone service'], n_samples, p=[0.42, 0.48, 0.10]),
    'InternetService': np.random.choice(['DSL', 'Fiber optic', 'No'], n_samples, p=[0.34, 0.44, 0.22]),
    'OnlineSecurity': np.random.choice(['Yes', 'No', 'No internet service'], n_samples, p=[0.28, 0.50, 0.22]),
    'OnlineBackup': np.random.choice(['Yes', 'No', 'No internet service'], n_samples, p=[0.34, 0.44, 0.22]),
    'DeviceProtection': np.random.choice(['Yes', 'No', 'No internet service'], n_samples, p=[0.34, 0.44, 0.22]),
    'TechSupport': np.random.choice(['Yes', 'No', 'No internet service'], n_samples, p=[0.29, 0.49, 0.22]),
    'StreamingTV': np.random.choice(['Yes', 'No', 'No internet service'], n_samples, p=[0.38, 0.40, 0.22]),
    'StreamingMovies': np.random.choice(['Yes', 'No', 'No internet service'], n_samples, p=[0.39, 0.39, 0.22]),
    'Contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_samples, p=[0.55, 0.21, 0.24]),
    'PaperlessBilling': np.random.choice(['Yes', 'No'], n_samples, p=[0.59, 0.41]),
    'PaymentMethod': np.random.choice(
        ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'],
        n_samples,
        p=[0.33, 0.23, 0.22, 0.22]
    ),
    'MonthlyCharges': np.random.uniform(18.25, 118.75, n_samples).round(2),
    'TotalCharges': np.random.uniform(18.8, 8684.8, n_samples).round(2),
    'Churn': np.random.choice(['Yes', 'No'], n_samples, p=[0.27, 0.73])
}

# Create DataFrame
df = pd.DataFrame(data)

# Add some missing values to TotalCharges
df.loc[np.random.choice(df.index, 11, replace=False), 'TotalCharges'] = np.nan

# Save to CSV
output_path = 'telecom_churn_sample.csv'
df.to_csv(output_path, index=False)

print(f"Sample telecom churn dataset created: {output_path}")
print(f"Shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head(10))
print(f"\nDataset info:")
print(df.info())
print(f"\nChurn distribution:")
print(df['Churn'].value_counts())
print(f"\nMissing values:")
print(df.isnull().sum())
