# PhishGuard-AI

An **AI-powered phishing detection system** designed to identify malicious websites using **machine learning** techniques and provide real-time risk assessments through an intuitive **Streamlit** interface.

## 🚀 Features
- **AI-Driven Detection:** Uses **XGBoost** for accurate phishing detection.
- **User-Friendly Interface:** Built with **Streamlit** for an interactive and easy-to-use experience.
- **Risk Scoring System:** Provides:
  - ✅ Clear risk scores
  - ✅ Confidence levels
  - ✅ Warning messages for better understanding
- **Real-Time URL Analysis:** Users can input URLs directly for instant results.
- **Visual Indicators:** Displays color-coded results (🔴 Phishing, 🟢 Safe) with relevant icons for clarity.
- **Robust Preprocessing:** Ensures data is cleaned, normalized, and engineered for optimal performance.

## 🛠️ Tech Stack
- **Python**
- **Machine Learning**
- **Streamlit** (for UI/UX)
- **Pandas & NumPy** (for data manipulation)
- **Joblib** (for model deployment)

## 📂 Project Structure
```
PhishGuard-AI/
├── data_preprocessing.py   # Data cleaning and feature engineering
├── model_training.py       # ML model training and saving the model
├── app.py                  # Streamlit app for user interaction
├── phishing_model.pkl      
├── Phishing.csv            # Dataset
├── requirements.txt        # Dependencies for the project
└── README.md               # Project documentation
```

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/realakshatkumar/PhishGuard-AI.git
   cd PhishGuard-AI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## ⚙️ Usage
1. Launch the Streamlit app.
2. Enter the URL you want to analyze in the provided input field.
3. Click **`Predict`** to view the result:
   - 🟢 **Safe** websites are shown in **green**.
   - 🔴 **Phishing** websites are highlighted in **red** with a warning message.

## 📊 Model Performance
- **Accuracy:** 89.87%
- **Precision & Recall:** Achieved through effective feature engineering and hyperparameter tuning.

## 📌 Future Improvements
✅ Enhance UI/UX with improved visual elements.  
✅ Implement a **URL Scraper** for extracting features from unknown URLs.  
✅ Integrate **real-time threat intelligence** for dynamic detection.  

## 🤝 Contributing
Contributions are welcome! Feel free to raise issues, suggest improvements, or create pull requests.


## 📬 Contact
For inquiries, reach out to **[realakshatkumar](https://github.com/realakshatkumar)** on GitHub. 😊

