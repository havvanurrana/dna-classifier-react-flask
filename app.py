from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Model ve vectorizer yükle
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    dna_seq = data.get("sequence", "")

    # DNA dizisini vectorizer ile dönüştür
    X = vectorizer.transform([dna_seq])
    prediction = model.predict(X)[0]

    result = "Healthy"
    valid_bases = set("ATCG")
    if any(base not in valid_bases for base in dna_seq):
        return jsonify({"prediction": "Mutant"})
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
