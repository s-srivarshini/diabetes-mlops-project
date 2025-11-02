# 🩺 Diabetes Prediction MLOps Project

This project is an end-to-end **Machine Learning + MLOps system** for predicting diabetes using the Pima Indians Diabetes Dataset.

It includes:

- ✅ Data preprocessing & EDA
- ✅ Model training (Random Forest)
- ✅ ML model saving & loading
- ✅ FastAPI for model inference
- ✅ Local testing with Swagger UI
- ✅ Docker (coming soon)
- ✅ MLflow experiment tracking (coming soon)
- ✅ CI/CD pipeline (coming soon)

---

## 📂 Project Structure

diabetes-project/
├── app/
│ └── main.py # FastAPI app
├── models/
│ └── diabetes_model.pkl # Saved ML model
├── notebooks/
│ └── training.ipynb # EDA + training notebook
├── src/
│ └── train.py # Training script
├── data/
│ └── diabetes.csv # Dataset (not uploaded to GitHub)
├── requirements.txt
└── README.md


---

## 📊 Dataset

**Source:** Pima Indians Diabetes Dataset  
You can download from:

- Kaggle: `https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database`
- UCI ML Repository

> ⚠ Dataset is not included in repo — download and place inside `data/`

---

## 🚀 Model Training

Run the training script:

```bash
python src/train.py


This will create:
models/diabetes_model.pkl

🧠 Tech Stack
Component	Tool
Language	Python 3.8+
Model	RandomForestClassifier
API	FastAPI
Testing UI	Swagger (/docs)
Version Control	Git + GitHub
▶️ Run FastAPI Server

From project root:

uvicorn app.main:app --reload

Test API

Open in browser:

http://127.0.0.1:8000/docs


Use sample input:

{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 79,
  "BMI": 28.5,
  "DiabetesPedigreeFunction": 0.35,
  "Age": 33
}
