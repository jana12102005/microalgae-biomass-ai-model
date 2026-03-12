from flask import Flask, render_template, request, jsonify
import torch
import torch.nn as nn
import numpy as np
import joblib

app = Flask(__name__)

# -------------------------------
# Load scaler
# -------------------------------
scaler = joblib.load("scaler.pkl")

# -------------------------------
# Neural Network Model
# -------------------------------
class AlgaeModel(nn.Module):
    def __init__(self):
        super(AlgaeModel, self).__init__()

        self.network = nn.Sequential(
            nn.Linear(7, 128),
            nn.ReLU(),

            nn.Linear(128, 64),
            nn.ReLU(),

            nn.Linear(64, 32),
            nn.ReLU(),

            nn.Linear(32, 1)
        )

    def forward(self, x):
        return self.network(x)

# -------------------------------
# Load trained model
# -------------------------------
model = AlgaeModel()
model.load_state_dict(torch.load("algae_model.pt", map_location="cpu"))
model.eval()

# -------------------------------
# Routes
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html")

# -------------------------------
# Prediction API
# -------------------------------

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        inputs = np.array([[

            float(data["Light"]),
            float(data["Nitrate"]),
            float(data["Iron"]),
            float(data["Phosphate"]),
            float(data["Temperature"]),
            float(data["pH"]),
            float(data["CO2"])

        ]])

        # scale input
        inputs_scaled = scaler.transform(inputs)

        tensor_input = torch.tensor(inputs_scaled, dtype=torch.float32)

        # inference
        with torch.no_grad():
            prediction = model(tensor_input).item()

        population = round(prediction, 2)

        # -------------------------------
        # Calculate CO2 absorption efficiency
        # -------------------------------
        efficiency = min((population / 5000) * 100, 100)

        # -------------------------------
        # Check if optimization needed
        # -------------------------------
        optimization = None

        if population < 3500:

            optimization = {

                "Light": 300,
                "Nitrate": 50,
                "Iron": 3,
                "Phosphate": 20,
                "Temperature": 28,
                "pH": 7.5,
                "CO2": 4

            }

        return jsonify({

            "population": population,
            "co2_efficiency": round(efficiency, 2),
            "optimization": optimization

        })

    except Exception as e:
        return jsonify({"error": str(e)})

# -------------------------------
# Separate Optimization API
# -------------------------------

@app.route("/optimize", methods=["POST"])
def optimize():

    suggestions = {

        "Light": 300,
        "Nitrate": 50,
        "Iron": 3,
        "Phosphate": 20,
        "Temperature": 28,
        "pH": 7.5,
        "CO2": 4

    }

    return jsonify(suggestions)

# -------------------------------
# Run Flask
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)