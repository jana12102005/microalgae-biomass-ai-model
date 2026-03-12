# 🌱 AI-Driven Microalgal Biomass Prediction & Bioreactor Simulator

This project presents an **AI-based predictive modeling system** for estimating microalgal biomass productivity under different environmental and nutrient conditions. The system integrates **Deep Learning, Flask, and an interactive visualization dashboard** to simulate microalgal growth and carbon sequestration efficiency.

Users can modify cultivation parameters and observe predicted biomass growth through a simulated **bioreactor environment** with real-time visualization.

---

## 🚀 Features

- AI-based **microalgal biomass prediction model**
- **Deep Learning neural network** built using PyTorch
- Interactive **Flask web application**
- Animated **bioreactor growth simulation**
- **CO₂ absorption efficiency meter**
- **Live biomass growth curve**
- **AI optimization suggestions** for improving cultivation parameters

---

## 🧠 AI Model

The predictive model uses a **Deep Neural Network (DNN)** trained on environmental and nutrient parameters affecting microalgal growth.

### Input Parameters
- Light Intensity (µmol m⁻² s⁻¹)
- Nitrate (mg/L)
- Iron (mg/L)
- Phosphate (mg/L)
- Temperature (°C)
- pH
- CO₂ Concentration (%)

### Output
- Predicted **Microalgal Population Density**
- Estimated **Carbon Sequestration Efficiency**

Population density acts as a **proxy indicator for biomass productivity**.

---

## 🧪 Methodology

1. Data collection from microalgae experimental datasets  
2. Data preprocessing and feature scaling  
3. Deep learning model training  
4. Model validation and evaluation  
5. Deployment through Flask web application  
6. Interactive visualization and simulation dashboard  

---

## 📊 System Architecture

User Input (Environmental Parameters)  
↓  
Flask Backend  
↓  
Deep Learning Prediction Model  
↓  
Population Prediction  
↓  
Bioreactor Visualization  
↓  
CO₂ Efficiency Meter + Growth Curve  
↓  
AI Optimization Suggestions  

---

## 📂 Project Structure

```
microalgae-biomass-ai-model
│
├── app.py
├── train.py
├── scaler.pkl
├── algae_model.pt
├── algeas.csv
│
├── templates
│   └── index.html
│
├── static
│   ├── style.css
│   └── algae.js
│
└── validation
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/jana12102005/microalgae-biomass-ai-model.git
cd microalgae-biomass-ai-model
```

Install dependencies:

```bash
pip install flask torch numpy scikit-learn joblib
```

---

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000
```

---

## 🌍 Applications

- Microalgae cultivation optimization  
- Carbon capture and climate mitigation research  
- Biofuel production studies  
- Sustainable biotechnology systems  
- Environmental modeling and simulation  

---

## 🔬 Future Work

- Lipid production prediction models  
- Real-time photobioreactor monitoring integration  
- Environmental data integration  
- AI-based parameter sensitivity analysis  
- Multi-species microalgae growth modeling  

---

## 👨‍🔬 Author

Janarthana  
AI & Green Biotechnology Project  
Microalgal Carbon Sequestration and Biomass Prediction System
