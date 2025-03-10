import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load the dataset
data = pd.read_csv('dataset/phishing.csv')

# Feature selection - Corrected column names
features = [
    'URL_Length', 'having_At_Symbol', 'Prefix_Suffix',
    'SSLfinal_State', 'Domain_registeration_length',
    'Request_URL', 'Submitting_to_email', 'age_of_domain',
    'web_traffic', 'Google_Index'
]

# Define Features (X) and Target (y)
X = data[features]
y = data['Result']  # Target variable (1 = Phishing, -1 = Legitimate)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Feature Scaling (Important for model performance)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Save the preprocessed data for model training
joblib.dump((X_train, X_test, y_train, y_test), 'dataset/preprocessed_data.pkl')

print("✅ Data preprocessing completed successfully!")
