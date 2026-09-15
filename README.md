# 🏥 Insurance Premium Prediction

An end-to-end Machine Learning application that predicts an insurance premium category — **Low, Medium, or High** — based on user and lifestyle information.

## 🚀 Live Demo

**Streamlit Frontend:**
https://insurance-premium-prediction-abvqej27q9catlzx5c3f5w.streamlit.app/

**FastAPI Backend:**
https://insurance-premium-api-y9ht.onrender.com/

**API Documentation:**
https://insurance-premium-api-y9ht.onrender.com/docs

## 📌 Project Overview

This project uses a **Random Forest Classifier** to predict an individual's insurance premium category from factors such as:

* Age group
* BMI
* Annual income
* City tier
* Occupation
* Lifestyle risk

The complete application follows an end-to-end ML deployment workflow:

**Data → Preprocessing → Model Training → Hyperparameter Tuning → Prediction API → Docker → Cloud Deployment → Streamlit UI**

## 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest
* ColumnTransformer
* OneHotEncoder
* Cross Validation
* Hyperparameter Tuning

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Frontend

* Streamlit

### Deployment

* Docker
* Render
* Streamlit Community Cloud

## 🤖 Machine Learning Model

The final model is a **Random Forest Classifier** with the following tuned parameters:

```text
n_estimators = 500
max_depth = 7
max_features = sqrt
min_samples_split = 2
min_samples_leaf = 1
```

The preprocessing and model are combined into a single pipeline and saved using `pickle`.

## 📊 Model Performance

Test Accuracy:

**72%**

Cross-validation Accuracy:

**~70.67%**

The model predicts three categories:

```text
Low
Medium
High
```

## 🔌 API

The FastAPI backend exposes a `/predict` endpoint.

Example workflow:

```text
Streamlit
    ↓
POST /predict
    ↓
FastAPI
    ↓
Preprocessing Pipeline
    ↓
Random Forest Model
    ↓
Prediction
    ↓
Streamlit
```

## 🐳 Docker

The FastAPI backend is containerized using Docker.

The Docker container runs the FastAPI application using Uvicorn:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## 📁 Project Structure

```text
insurance-premium-prediction/
│
├── model/
│   ├── predict.py
│   └── model.pkl
│
├── schema/
│   └── userInput.py
│
├── app.py
├── frontend.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd insurance-premium-prediction
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start FastAPI

```bash
uvicorn app:app --reload
```

API:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

### 6. Start Streamlit

```bash
streamlit run streamlit_app.py
```

## 🎯 Key Learning Outcomes

* Built an ML classification pipeline
* Performed feature preprocessing
* Used Random Forest for classification
* Applied cross-validation and hyperparameter tuning
* Serialized the trained pipeline using pickle
* Built a REST API using FastAPI
* Containerized the application using Docker
* Connected a Streamlit frontend to a deployed API
* Deployed the backend and frontend to the cloud

## 👨‍💻 Author

**Sanmaya Pandua**

MCA | Data Science & Machine Learning
