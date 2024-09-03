import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a DataFrame
file_path = '.\datasets\social media dataset.xlsx'  # Replace with your Excel file path
df = pd.read_excel(file_path)

# Function to count responses
def count_responses(df, column_name):
    return df[column_name].value_counts()

# Define the columns of interest based on your dataset
columns_of_interest = [
    "Is social media a valuable tool for educational purposes?",
    "Should students be cautious about sharing personal information on social media platforms?",
    "Can excessive use of social media negatively impact academic performance?",
    "Is it important for students to actively manage their online privacy settings?",
    "Does social media contribute to building and maintaining friendships?",
    "Should students be aware of the potential risks associated with online interactions on social media?",
    "Is it necessary for students to allocate a specific time for social media use to balance with other responsibilities?",
    "Can social media have an impact on mental health, both positive and negative?",
    "Do students have a responsibility to fact-check information before sharing it on social media?",
    "Can social media be a platform for positive contributions to the community or society?"
]

# Plotting the responses
plt.figure(figsize=(30, 27))

for i, column in enumerate(columns_of_interest):
    plt.subplot(4, 3, i + 1)
    counts = count_responses(df, column)
    counts.plot(kind='bar', color=['skyblue', 'salmon'], edgecolor='black')
    plt.title(column)
    plt.xticks(rotation=45)
    plt.xlabel('Response')
    plt.ylabel('Count')

plt.tight_layout()
plt.show()