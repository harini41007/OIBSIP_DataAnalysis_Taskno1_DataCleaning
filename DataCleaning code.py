#Import libraries
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('AB_NYC_2019.csv') 
df.head()

#Basic inspection
df.info()
df.describe()

#Identify missing values
df.isnull().sum()

#Fill missing values with mean
num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

#Fill missing values with Nan
df['name'] = df['name'].fillna('Nan')
df['host_name'] = df['host_name'].fillna('Nan')
df['last_review'] = df['last_review'].fillna('No Review')

# Check duplicates
print("Duplicate Rows:", df.duplicated().sum())

#standardize columns 
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

#Define categorical columns 
cat_cols = df.select_dtypes(include='object').columns 
print(cat_cols)

#Standardize text 
for col in cat_cols: 
df[col] = df[col].str.lower().str.strip() 

#outlier detection 
numeric_cols = df.select_dtypes(include=np.number).columns 
numeric_cols

#detect outliers 
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"{col}: {len(outliers)} outliers")

#Remove outliers
def remove_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[col] >= lower) & (df[col] <= upper)]
# Apply to numerical columns
for col in num_cols:
    df = remove_outliers(df, col)

#visualize outliers
import seaborn as sns
import matplotlib.pyplot as plt
for col in num_cols:
    sns.boxplot(x=df[col])
    plt.title(col)
    plt.show()
