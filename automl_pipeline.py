import os
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from prefect import task, flow
import joblib

# Configuration
DATA_PATH = "data/dataset.csv"
MODEL_PATH = "models/model.pkl"

# Data Ingestion
@task
def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

# Data Preprocessing
@task
def preprocess_data(df):
    df = df.dropna()
    X = df.drop(columns=['target'])
    y = df['target']
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
@task
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)
    return model

# Model Evaluation
@task
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)
    return accuracy

# MLOps Pipeline
@flow
def mlops_pipeline():
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(df)
    model = train_model(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    print(f"Model Accuracy: {accuracy}")

if __name__ == "__main__":
    mlops_pipeline()
