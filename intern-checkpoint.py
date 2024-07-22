import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset using a raw string to handle backslashes in the file path
file_path = r'.ipynb_checkpoints\Updated_HR_Employee_Attrition.xlsx'
data = pd.read_excel(file_path)



# Data cleaning steps
data_cleaned = data.drop(columns=['EmployeeNumber'])
data_cleaned.columns = [col.lower().replace(' ', '_') for col in data_cleaned.columns]
data_cleaned.dropna(inplace=True)
data_cleaned['employee_attrition'] = data_cleaned['employeeattrition'].map({'Yes': 1, 'No': 0})

# Convert categorical variables to numerical for correlation analysis
categorical_columns = ['travelfrequency', 'workdepartment', 'fieldofstudy', 'maritalstatus', 'gender', 'overtime', 'jobrole', 'over18']
for column in categorical_columns:
    data_cleaned[column] = data_cleaned[column].astype('category').cat.codes

# Convert totalworkingyears to numeric, handling any remaining non-numeric entries
data_cleaned['totalworkingyears'] = pd.to_numeric(data_cleaned['totalworkingyears'], errors='coerce')

# Check for any non-numeric data in the DataFrame
print("Data types after conversion:")
print(data_cleaned.dtypes)

# Drop any remaining non-numeric columns
numeric_data = data_cleaned.select_dtypes(include=['int64', 'float64'])

# Correlation matrix
plt.figure(figsize=(12, 8))
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix for Numeric Variables')
plt.show()

# Distributions and relationships
# Overtime distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='overtime', data=data_cleaned)
plt.title('Overtime Distribution')
plt.xlabel('Overtime')
plt.ylabel('Count')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
plt.show()

# Marital Status distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='maritalstatus', data=data_cleaned)
plt.title('Marital Status Distribution')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.show()

# Job Role distribution
plt.figure(figsize=(12, 6))
sns.countplot(y='jobrole', data=data_cleaned, order=data_cleaned['jobrole'].value_counts().index)
plt.title('Job Role Distribution')
plt.xlabel('Count')
plt.ylabel('Job Role')
plt.show()

# Gender distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='gender', data=data_cleaned)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Education Field distribution
plt.figure(figsize=(12, 6))
sns.countplot(y='fieldofstudy', data=data_cleaned, order=data_cleaned['fieldofstudy'].value_counts().index)
plt.title('Education Field Distribution')
plt.xlabel('Count')
plt.ylabel('Education Field')
plt.show()

# Department distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='workdepartment', data=data_cleaned)
plt.title('Department Distribution')
plt.xlabel('Department')
plt.ylabel('Count')
plt.show()

# Business Travel distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='travelfrequency', data=data_cleaned)
plt.title('Business Travel Distribution')
plt.xlabel('Business Travel Frequency')
plt.ylabel('Count')
plt.show()

# Relation between Overtime and Age
plt.figure(figsize=(10, 6))
sns.boxplot(x='overtime', y='age', data=data_cleaned)
plt.title('Relation between Overtime and Age')
plt.xlabel('Overtime')
plt.ylabel('Age')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
plt.show()

# Relation between Overtime and Total Working Years
plt.figure(figsize=(10, 6))
sns.boxplot(x='overtime', y='totalworkingyears', data=data_cleaned)
plt.title('Relation between Overtime and Total Working Years')
plt.xlabel('Overtime')
plt.ylabel('Total Working Years')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
plt.show()

# Relation between Overtime and Number of Companies Worked
plt.figure(figsize=(10, 6))
sns.boxplot(x='overtime', y='numcompaniesworked', data=data_cleaned)
plt.title('Relation between Overtime and Number of Companies Worked')
plt.xlabel('Overtime')
plt.ylabel('Number of Companies Worked')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
plt.show()
