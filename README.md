# Heart Disease Prediction using Machine Learning 🫀🤖

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![Kaggle Dataset](https://img.shields.io/badge/Dataset-Kaggle-blue)](https://www.kaggle.com/ronitf/heart-disease-uci)

## 🔍 Overview

Heart disease is one of the leading causes of death globally. Early prediction and diagnosis are crucial for effective treatment and prevention. This project leverages **Machine Learning algorithms** to predict the presence of heart disease in patients based on a range of medical attributes.

The main goal of this project is to build reliable and accurate predictive models that can assist healthcare professionals in identifying high-risk individuals and ensuring timely intervention.

## 📊 Dataset

- **Source**: [Kaggle - Heart Disease UCI](https://www.kaggle.com/ronitf/heart-disease-uci)
- **Type**: Classification (Binary)
- **Target Variable**: `target` (1 = presence of heart disease, 0 = absence)
- **Features**: Age, Sex, Chest pain type, Resting BP, Cholesterol, Fasting Blood Sugar, etc.

## ⚙️ Machine Learning Models Used

The following algorithms were trained and evaluated on the dataset:

1. **Logistic Regression** (Scikit-learn)
2. **Naive Bayes** (Scikit-learn)
3. **Support Vector Machine (SVM)** - Linear kernel (Scikit-learn)
4. **K-Nearest Neighbours (KNN)** (Scikit-learn)
5. **Decision Tree** (Scikit-learn)
6. **Random Forest** (Scikit-learn)
7. **XGBoost** (XGBoost library)
8. **Artificial Neural Network (ANN)** - 1 Hidden Layer (Keras)

### ✅ Best Accuracy Achieved: **95%** (Random Forest)

## 📌 Features of the Project

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature selection and scaling
- Comparison of multiple ML algorithms
- Hyperparameter tuning
- Neural Network implementation with Keras
- Model evaluation metrics (Accuracy, Confusion Matrix, etc.)

## 🧪 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/abhi-tiwari-01/HeartDisease.git
   cd HeartDisease
   ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the app:
    ```bash
    streamlit run app.py
    ```
4. Open your web browser and navigate to `http://localhost:8501` to view the app.

## 📁 Project Structure
```plaintext
    HeartDisease
    ├── app.py
    ├── heart_disease_model.pkl
    ├── Heart_Disease_Prediction.ipynb   
    ├── heart.csv                       
    ├── README.md                 
    └── requirements.txt               
```
## 🧠 Future Enhancements
- Deploy the model as a web application using Flask or Streamlit

- Add more features or newer datasets for better generalization

- Perform cross-validation and deeper hyperparameter tuning

- Add feature importance analysis

## 🤝 Contributions
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🔗 Useful Links
[![Kaggle Dataset](https://img.shields.io/badge/Dataset-Kaggle-blue)](https://www.kaggle.com/ronitf/heart-disease-uci)

[![GitHub Repo](https://img.shields.io/badge/Repo-GitHub-black?logo=github)](https://github.com/abhi-tiwari-01/HeartDisease)
