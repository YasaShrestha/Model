import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from Excel file
file_path = '.\datasets\Effects of Social Media (Responses) (1).xlsx'
data = pd.read_excel(file_path, sheet_name='Effects of Social Media (Respon')

# Display the first few rows of the dataframe
print(data.head())

# Data Cleaning (if necessary)
# Ensure columns are named correctly and data is in the right format

# 1. Social Media Platform Usage
platforms = data['Which social media platform/s do you like the most or use the most?'].str.get_dummies(sep=', ')
platform_usage = platforms.sum().sort_values(ascending=False)

plt.figure(figsize=(20, 16))
sns.barplot(x=platform_usage.index, y=platform_usage.values, palette='viridis')
plt.title('Social Media Platform Usage')
plt.xlabel('Social Media Platform')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 2. Time Spent on Social Media
time_spent_mapping = {
    'upto 4 hrs': 4,
    'more than 4 hrs': 5,
    '1 - 2.5 hrs': 2.5,
    'none': 0
}

data['How much time do you spend on social media in a day?'] = data['How much time do you spend on social media in a day?'].map(time_spent_mapping)
plt.figure(figsize=(20, 16))
sns.histplot(data['How much time do you spend on social media in a day?'], bins=4, kde=False, color='skyblue')
plt.title('Histogram of Time Spent on Social Media')
plt.xlabel('Hours Spent on Social Media')
plt.ylabel('Frequency')
plt.show()

# 3. Exposure to Inappropriate Content
plt.figure(figsize=(20, 16))
sns.histplot(data['How much do you feel that you are exposed to inappropriate content on these platforms (out of 10)?'], bins=8, kde=False, color='coral')
plt.title('Exposure to Inappropriate Content')
plt.xlabel('Exposure Level (out of 10)')
plt.ylabel('Frequency')
plt.show()

# 4. Types of Cyber Crimes Experienced
cyber_crimes = data['Have you ever been a victim of any of these cyber crimes?'].value_counts()
plt.figure(figsize=(20, 16))
sns.barplot(x=cyber_crimes.index, y=cyber_crimes.values, palette='magma')
plt.title('Types of Cyber Crimes Experienced')
plt.xlabel('Type of Cyber Crime')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 5. Preferred Communication Types
communication_counts = data['Which type of communication do you generally prefer?'].value_counts()
plt.figure(figsize=(20, 16))
sns.barplot(x=communication_counts.index, y=communication_counts.values, palette='cividis')
plt.title('Preferred Communication Types')
plt.xlabel('Type of Communication')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()