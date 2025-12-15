"""
Generate a sample Titanic dataset for testing the multi-agent system.
This is a simplified version of the famous Titanic dataset.
"""
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Create sample Titanic-like dataset
n_samples = 891

data = {
    'PassengerId': range(1, n_samples + 1),
    'Survived': np.random.choice([0, 1], n_samples, p=[0.62, 0.38]),
    'Pclass': np.random.choice([1, 2, 3], n_samples, p=[0.24, 0.21, 0.55]),
    'Name': [f'Passenger_{i}' for i in range(1, n_samples + 1)],
    'Sex': np.random.choice(['male', 'female'], n_samples, p=[0.65, 0.35]),
    'Age': np.random.normal(29.7, 14.5, n_samples).clip(0.42, 80),
    'SibSp': np.random.choice([0, 1, 2, 3, 4, 5, 8], n_samples, p=[0.68, 0.23, 0.05, 0.02, 0.01, 0.005, 0.005]),
    'Parch': np.random.choice([0, 1, 2, 3, 4, 5, 6], n_samples, p=[0.76, 0.13, 0.08, 0.01, 0.01, 0.005, 0.005]),
    'Fare': np.random.gamma(2, 15, n_samples).clip(0, 512),
    'Embarked': np.random.choice(['C', 'Q', 'S'], n_samples, p=[0.19, 0.09, 0.72])
}

# Create DataFrame
df = pd.DataFrame(data)

# Add some missing values to simulate real data
df.loc[np.random.choice(df.index, 177, replace=False), 'Age'] = np.nan
df.loc[np.random.choice(df.index, 2, replace=False), 'Embarked'] = np.nan

# Round numerical columns
df['Age'] = df['Age'].round(1)
df['Fare'] = df['Fare'].round(2)

# Save to CSV
output_path = 'titanic_sample.csv'
df.to_csv(output_path, index=False)

print(f"Sample Titanic dataset created: {output_path}")
print(f"Shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head(10))
print(f"\nDataset info:")
print(df.info())
print(f"\nMissing values:")
print(df.isnull().sum())
