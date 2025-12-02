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

Powershell:
```powershell
Invoke-RestMethod -Uri https://bias-detector-2.onrender.com/predict -Method POST -ContentType "application/json" -Body '{"text":"The mayor is ruining our city!"}'
```
Linux/macOS terminal:
```powershell
curl -X POST https://bias-detector-2.onrender.com/predict -H "Content-Type: application/json" -d '{"text":"The mayor is ruining our city!"}'
```
# Design Decicions
## Why This Concept?
I wanted to try to find a way to incorporate journalism into this project in some way. Some of my other ideas originally included doing a topic classifier where users inputted a title and it told you if it were a sports, news, opinion, or life article or doing a fake news detector where you inputted a headline and it outputted the likelihood of the artically being factually correct. I ended up choosing my bias detector because it seemed like the most practical, since the first option wouldn't be too useful as readers are usually already able to tell what type of article it is that they're reading, and the second option would likely not give reliable results because there are a number of confounding variables that might influence the validity of the article, such as the publication.
## Tradeoffs
Choosing a bias classifier allowed for a manageable dataset and a clear ML workflow, but it comes with limitations. Using a simple TF-IDF + Logistic Regression pipeline trades off potential predictive performance for simplicity and interpretability. More complex models like transformers could improve accuracy but would increase computational cost, complexity, and deployment difficulty. Containerizing with Docker ensures reproducibility and ease of deployment, though it adds an extra step for users unfamiliar with Docker.
## Edge Cases
Since the model gives a weighted decimal output, headlines that don't fit into any one category are accounted for because they tend to give results that don't indicate too strong of any one type (all around .33). Potential edge cases do include empty or nonheadline responses or responses that are too long. To handle empty responses, the API returns a clear error message indicating that no text was provided. For excessively long headlines, the text is truncated to a reasonable length to prevent processing issues. Non-text input, such as numbers or HTML code, is cleaned and normalized before being passed to the model, ensuring that the API does not crash and provides a consistent prediction format. These safeguards make the service robust to unusual or unexpected input while maintaining reliable output.
## Security/Privacy:
The project avoids storing or exposing sensitive information. No API keys, passwords, or PII are included; the .env.example file demonstrates environment variable usage without secrets. Input validation is minimal but ensures that only text strings are processed. Since the model only analyzes headlines or short text snippets, there is no handling of personal user data, and predictions are transient, reducing privacy risks.
## Ops
The application logs basic information for debugging, such as incoming requests and prediction outcomes. Scaling considerations include running multiple Docker containers behind a load balancer if needed, though this project is intended for local or small-scale use. Known limitations include potential bias in predictions due to the dataset size and class distribution, and lack of advanced monitoring or alerting. Future improvements could add structured logging, metrics collection, and automated testing for operational reliability.
# Results & Evaluation
![Bias Detector Examples](assets/RyanBias-DetectorExamples.png)

This shows the headlines of three of my articles that I've written for The Cavalier Daily, one balanced, one provocative, and one partisan. 
I inputted each of these into the model, and it outputted the results shown above for each one, which i think are mostly accurate. The top one is a sports-angled article that is not really partisan and not as provocative as it is balanced, and the model correctly identified that it was balanced, with provocative being the second most likely option. The middle one is an article I did on homelessness, where the title, "Charlottesville needs to embrace a comprehensive solution to homelessness", leaves readers wondering what this solution should be, so it is a provocative headline, which the model correctly identified. The bottom headline is an article that explains how the university should defend against actions from the federal government, and the model correctly identified it as partisan
# What's Next
While the current Bias Detector demonstrates the core pipeline, several improvements and extensions are possible and could be done in the future:
- Model Improvements: Experiment with larger datasets, different text embeddings, or more advanced classifiers to improve accuracy and reduce misclassifications.
- Expanded Labels: Introduce finer-grained bias categories or multi-label predictions for nuanced articles.
- User Interface: Build a simple web front-end for users to input headlines without using curl or terminal commands.
# Links
Github Repo: https://github.com/hbz4cf/bias-detector

Cloud Deployment: https://bias-detector-2.onrender.com (see 'How to Run' Section for use)








