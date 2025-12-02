from flask import Flask, request, jsonify
import joblib
import os

# Paths
MODEL_PATH = "../assets/model.joblib"

# Load the trained model
pipeline = joblib.load(os.path.join(os.path.dirname(__file__), MODEL_PATH))

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    prediction = pipeline.predict([text])[0]
    probabilities = pipeline.predict_proba([text])[0]
    labels = pipeline.classes_
    prob_dict = {label: float(probabilities[i]) for i, label in enumerate(labels)}

    return jsonify({
        "headline": text,
        "prediction": prediction,
        "probabilities": prob_dict
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
