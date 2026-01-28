from os import dup
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
#columns names
columns= [
    'age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target'
    ]
#load the dataset
df = pd.read_csv(url, names=columns)

#display first few rows
print("Dataset Preview")
display(df)

#check missing values
df.replace('?', pd.NA, inplace = True)
display(df)

#missing values in each column
missing_values = df.isna().sum()
print(missing_values)

#total missing values
print(df.isna().sum().sum())

#duplicate row check

#check number of duplicate rows
duplicate_count = df.duplicated().sum();
print(duplicate_count)

#display duplicate rows
if duplicate_count > 0:
  print("\nDuplicate rows:")
  display(df[df.duplicated()])
else:
  print("\nNo duplicated rows found.")

#remove duplicates
df.drop_duplicates()