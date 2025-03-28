import pandas as pd  # 📊 Import Pandas for handling data
import numpy as np  # 🔢 Import NumPy for numerical operations
from sklearn.linear_model import LinearRegression  # 🤖 Import Linear Regression Model from scikit-learn
import subprocess  # 💻 Allows us to run system commands (like Terraform commands)

# 📌 Step 1: Sample Traffic Data (Replace this with real data later)
data = {
    "hour": np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                      13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]),  # 🕒 Hours of the day (0 to 23)
    "traffic": np.array([30, 25, 20, 15, 10, 5, 10, 30, 60, 100, 150, 200, 250,
                         300, 350, 320, 280, 400, 450, 420, 380, 200, 100, 50])  # 🚗 Traffic volume per hour
}

# 📌 Step 2: Convert the data into a DataFrame (like an Excel table)
df = pd.DataFrame(data)

# 📌 Step 3: Define Features (X) & Target (y)
X = df[['hour']]  # ⏳ X = Hour of the day (Input Feature)
y = df['traffic']  # 🚦 y = Traffic volume (Target Variable)

# 📌 Step 4: Train a Linear Regression Model
model = LinearRegression()  # 🎯 Create a Linear Regression model
model.fit(X, y)  # 🏋️‍♂️ Train the model using the dataset (X = hours, y = traffic)

# 📌 Step 5: Predict traffic for the next hour (Example: Hour 24, next day)
next_hour = np.array([[24]])  # 🕛 Predict for hour 24
predicted_traffic = model.predict(pd.DataFrame(next_hour, columns=["hour"]))[0]  # 🔮 Get the predicted traffic value

# 📌 Step 6: Decide how many containers to scale based on traffic 🚀
if predicted_traffic < 100:
    num_containers = 1  # 🟢 Light Traffic → Use 1 container
elif 100 <= predicted_traffic < 300:
    num_containers = 2  # 🟡 Medium Traffic → Use 2 containers
else:
    num_containers = 3  # 🔴 Heavy Traffic → Use 3 containers

# 🔥 Print Predicted Traffic and Scaling Decision
print(f"Predicted Traffic: {predicted_traffic}")
print(f"Scaling to {num_containers} containers...")

# 📌 Step 7: Update Terraform Variables (terraform.tfvars file)
with open("terraform.tfvars", "w") as f:
    f.write(f'num_containers = "{num_containers}"\n')  # 📝 Write the new container count into terraform.tfvars

# 📌 Step 8: Run Terraform to Apply Scaling Changes
subprocess.run(["terraform", "apply", "-auto-approve"], check=True)  # 🚀 Apply Terraform changes automatically
