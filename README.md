# MLOps-Flow

This repository contains an advanced MLOps pipeline that automates the lifecycle of a machine learning model. The pipeline includes:
Data Ingestion: Loads data from CSV files.
Data Preprocessing: Cleans and prepares the dataset for training.
Model Training: Trains a Random Forest Classifier.
Model Evaluation: Computes accuracy and logs metrics with MLflow.
CI/CD for ML: Automates model validation and deployment.
Model Deployment: Uses FastAPI and Docker to serve the model.
Monitoring & Logging: Uses Prometheus and Grafana for observability.
Model Retraining: Automatically retrains the model based on performance drift.

Installation

Clone the repository:

git clone https://github.com/futehc/mlops-pipeline.git
cd mlops-pipeline

Install dependencies:

pip install -r requirements.txt

Usage

Run the MLOps pipeline:

python pipeline.py

Model Deployment

Build and run the Docker container:

docker build -t mlops-pipeline .
docker run -p 8080:8080 mlops-pipeline

Monitoring

Start Prometheus and Grafana:

docker-compose up -d

CI/CD Integration

The pipeline includes CI/CD automation using GitHub Actions and Jenkins. To trigger model training and deployment, push changes to the repository:

git push origin main

License
MIT License
