# Executive Summary:
As an opinion editor for UVA's newspaper, I regularly evaluate headlines not just for clarity but for tone, bias, and potential reader impact. This project builds a lightweight Bias Detector that automates part of that process by classifying opinion headlines into Balanced, Partisan, or Provocative categories. The tool is designed to help writers and editors become more aware of language that may inadvertently push a narrative or heighten polarization.
# System Overview:
## Course concepts
This project demonstrates bias classification by integrating multiple course concepts: it uses a data pipeline built with pandas for dataset loading and preprocessing, a machine learning pipeline with scikit-learn (TF-IDF vectorization + Logistic Regression) for training and evaluation, and a Flask API for serving predictions. The application is fully containerized using Docker, ensuring reproducibility and easy deployment.
## Architecture Diagram
![Architecture Diagram](assets/architecture.png.png)
## Data/Models/Services
The project uses a curated opinion dataset stored in assets/opinion_dataset.csv containing 105 labeled articles for training and testing the bias classifier. The CSV is in standard text format, roughly 7 KB in size, and does not have licensing restrictions as it was created for instructional purposes. The trained model is saved as assets/model.joblib, a binary file of about 20 KB that stores the TF-IDF vectorizer and Logistic Regression classifier pipeline. The model was trained locally using Python 3.11 with scikit-learn and pandas, and it is intended for educational and demonstration purposes only. All project services, including the API in src/api.py and containerization via the Dockerfile, are open-source and rely on permissively licensed Python libraries (Flask, joblib, scikit-learn, pandas).
# How to Run (Local)
Run the Bias Detector locally using Docker. Make sure Docker is installed and `.env` is configured.
```bash
# Build Docker image
docker build -t bias-detector:latest .
# Run container
docker run --rm -p 8080:8080 --env-file .env bias-detector:latest
# Health check
curl http://localhost:8080/health
# Make a prediction
curl -X POST http://localhost:8080/predict \
-H "Content-Type: application/json" \
-d '{"text":"The mayor is ruining our city!"}'
```
# Design Decicions
## Why This Concept?
I wanted to try to find a way to incorporate journalism into this project in some way. Some of my other ideas originally included doing a topic classifier where users inputted a title and it told you if it were a sports, news, opinion, or life article or doing a fake news detector where you inputted a headline and it outputted the likelihood of the artically being factually correct. I ended up choosing my bias detector because it seemed like the most practical, since the first option wouldn't be too useful as readers are usually already able to tell what type of article it is that they're reading, and the second option would likely not give reliable results because there are a number of confounding variables that might influence the validity of the article, such as the publication.
## Tradeoffs
Choosing a bias classifier allowed for a manageable dataset and a clear ML workflow, but it comes with limitations. Using a simple TF-IDF + Logistic Regression pipeline trades off potential predictive performance for simplicity and interpretability. More complex models like transformers could improve accuracy but would increase computational cost, complexity, and deployment difficulty. Containerizing with Docker ensures reproducibility and ease of deployment, though it adds an extra step for users unfamiliar with Docker.
## Security/Privacy:
The project avoids storing or exposing sensitive information. No API keys, passwords, or PII are included; the .env.example file demonstrates environment variable usage without secrets. Input validation is minimal but ensures that only text strings are processed. Since the model only analyzes headlines or short text snippets, there is no handling of personal user data, and predictions are transient, reducing privacy risks.
## Ops
The application logs basic information for debugging, such as incoming requests and prediction outcomes. Scaling considerations include running multiple Docker containers behind a load balancer if needed, though this project is intended for local or small-scale use. Known limitations include potential bias in predictions due to the dataset size and class distribution, and lack of advanced monitoring or alerting. Future improvements could add structured logging, metrics collection, and automated testing for operational reliability.

