import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset from Excel
file_path = '.\datasets\Effects of Social Media (Responses) (1).xlsx'
df = pd.read_excel(file_path)  # Replace with your file path

# Display the first few rows
print(df.head())

# Drop rows with missing values (if any)
df = df.dropna()

# Encode categorical variables
label_encoders = {}
categorical_columns = [
    'Which social media platform/s do you like the most or use the most?',
    'How much time do you spend on social media in a day?',
    'How much time do you spend on physical activities in a day?',
    'Which type of communication do you generally prefer?'
]

for column in categorical_columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Encode the target variable
df['Have you ever been a victim of any of these cyber crimes?'] = df['Have you ever been a victim of any of these cyber crimes?'].apply(
    lambda x: 1 if x != 'None of the above' else 0
)

# Split data into features and target
X = df.drop(['Timestamp', 'Have you ever been a victim of any of these cyber crimes?'], axis=1)
y = df['Have you ever been a victim of any of these cyber crimes?']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build and train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))