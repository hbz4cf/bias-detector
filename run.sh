#!/bin/bash
# run.sh - Reproducible launcher for Bias Detector project

# 1. Activate the virtual environment
source ./venv/Scripts/activate

# 2. Train the model and save it
echo "Training model and saving to ./assets/model.joblib..."
python src/pipeline.py

# 3. Start the API
echo "Starting Flask API on localhost:8080..."
python src/api.py

Invoke-RestMethod -Uri http://localhost:8080/predict -Method POST -ContentType "application/json" -Body '{"text":"(INSERT HEADLINE)"}'
