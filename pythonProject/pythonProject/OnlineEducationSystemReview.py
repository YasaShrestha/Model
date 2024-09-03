import pandas as pd

# Load the data from CSV
file_path = '.\datasets\ONLINE EDUCATION SYSTEM REVIEW.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(df.head())

# Basic information about the dataset
print("\nBasic Information:")
print(df.info())

# Statistical summary of numerical columns
print("\nStatistical Summary:")
print(df.describe())

# Count of unique values in categorical columns
print("\nUnique Values in Categorical Columns:")
for column in df.select_dtypes(include=['object']).columns:
    print(f"{column}:")
    print(df[column].value_counts())

# Analyzing the level of satisfaction in Online Education
print("\nLevel of Satisfaction Distribution:")
print(df['Your level of satisfaction in Online Education'].value_counts())

# Analyzing average marks scored before pandemic by level of satisfaction
print("\nAverage Marks Scored by Satisfaction Level:")
print(df.groupby('Your level of satisfaction in Online Education')['Average marks scored before pandemic in traditional classroom'].value_counts())

# Analyze the average study time by satisfaction level
print("\nAverage Study Time by Satisfaction Level:")
print(df.groupby('Your level of satisfaction in Online Education')['Study time (Hours)'].mean())

# Analyze the relationship between study time and performance in online education
import seaborn as sns
import matplotlib.pyplot as plt

print("\nStudy Time vs. Online Performance:")
sns.boxplot(data=df, x='Performance in online', y='Study time (Hours)')
plt.title('Study Time vs. Online Performance')
plt.show()