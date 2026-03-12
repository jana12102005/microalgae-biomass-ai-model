import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error

# -------------------------------
# 1️⃣ LOAD DATA
# -------------------------------

data_path = r"A:\Microalgal Carbon Sequestration\ma\algeas.csv"
df = pd.read_csv(data_path)

print("Dataset Shape:", df.shape)
print(df.head())

# -------------------------------
# 2️⃣ FEATURES & TARGET
# -------------------------------

X = df.drop(columns=["Population"]).values
y = df["Population"].values

# -------------------------------
# 3️⃣ TRAIN / TEST SPLIT
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 4️⃣ NORMALIZATION (CRITICAL)
# -------------------------------

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert to tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
y_test = torch.tensor(y_test, dtype=torch.float32).view(-1, 1)

# -------------------------------
# 5️⃣ MODEL DEFINITION
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

model = AlgaeModel()

# -------------------------------
# 6️⃣ LOSS & OPTIMIZER
# -------------------------------

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# -------------------------------
# 7️⃣ TRAINING LOOP
# -------------------------------

epochs = 100
batch_size = 64

for epoch in range(epochs):
    
    permutation = torch.randperm(X_train.size()[0])
    
    for i in range(0, X_train.size()[0], batch_size):
        indices = permutation[i:i+batch_size]
        
        batch_x = X_train[indices]
        batch_y = y_train[indices]
        
        optimizer.zero_grad()
        
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        
        loss.backward()
        optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{epochs}] Loss: {loss.item():.4f}")

# -------------------------------
# 8️⃣ EVALUATION
# -------------------------------

model.eval()
with torch.no_grad():
    predictions = model(X_test)

predictions_np = predictions.numpy()
y_test_np = y_test.numpy()

r2 = r2_score(y_test_np, predictions_np)
mse = mean_squared_error(y_test_np, predictions_np)

print("\nModel Performance:")
print("R² Score:", r2)
print("MSE:", mse)

# -------------------------------
# 9️⃣ SAVE MODEL & SCALER
# -------------------------------

torch.save(model.state_dict(), "algae_model.pt")

import joblib
joblib.dump(scaler, "scaler.pkl")

print("\n✅ Model & Scaler Saved Successfully")
