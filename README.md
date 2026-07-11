# 🛍️ Fake Product Review Detection using Machine Learning

## 📌 Overview

Fake Product Review Detection is a Machine Learning project that classifies product reviews as **Fake** or **Genuine** using Natural Language Processing (NLP). The project preprocesses review text, extracts meaningful features using TF-IDF, and applies a machine learning classifier to identify deceptive reviews. It helps improve the reliability of online reviews and supports better purchasing decisions.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Matplotlib
- Joblib

---

## 📂 Dataset

The model is trained on a labeled dataset containing product reviews and their corresponding class labels (Fake or Genuine).

---

## 📊 Machine Learning Pipeline

- Data Cleaning and Preprocessing
- Text Vectorization using TF-IDF
- Model Training
- Model Evaluation
- Model Saving
- Prediction on New Reviews

---

## 📸 Screenshots

The `screenshots/` folder contains project output images and prediction results.

---

## ▶️ Installation

```bash
git clone https://github.com/yourusername/Fake-Review-Detection.git

cd Fake-Review-Detection

pip install -r requirements.txt
```

## ▶️ Run

Run the application:

```bash
streamlit run review.py
```
