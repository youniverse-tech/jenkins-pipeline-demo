import os
import re
import joblib
import numpy as np
from sklearn.ensemble import IsolationForest

# Ensure UTF-8 encoding for Windows
os.environ["PYTHONUTF8"] = "1"

# File paths
log_file_path = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Jenkins-Pipeline-Demo\\jenkins.log"
filtered_log_file = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Jenkins-Pipeline-Demo\\filtered_logs.txt"
anomaly_log_file = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Jenkins-Pipeline-Demo\\anomalies.txt"
model_file = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Jenkins-Pipeline-Demo\\log_anomaly_model.pkl"

# Define log levels to filter
log_levels_to_filter = ["SEVERE", "WARNING", "ERROR"]
log_pattern = re.compile(r"\b(SEVERE|WARNING|ERROR)\b")

def filter_logs(log_file, levels, output_file):
    """Filters logs containing specified levels and saves them."""
    filtered_logs = []
    try:
        with open(log_file, "r", encoding="utf-8") as file:
            for line in file:
                if any(level in line for level in levels):
                    filtered_logs.append(line.strip())

        with open(output_file, "w", encoding="utf-8") as output:
            output.write("\n".join(filtered_logs))

        print(f"✅ Filtered logs saved in: {output_file}")
        return filtered_logs
    except FileNotFoundError:
        print(f"❌ Log file not found at: {log_file}")
        return []

def extract_features(logs):
    """Converts logs into numerical features for AI anomaly detection."""
    features = []
    for log in logs:
        length = len(log)
        uppercase_ratio = sum(1 for c in log if c.isupper()) / max(1, length)
        special_chars = sum(1 for c in log if not c.isalnum() and c != " ") / max(1, length)
        features.append([length, uppercase_ratio, special_chars])
    return np.array(features)

def detect_anomalies(logs):
    """Detects anomalies using Isolation Forest with better training."""
    if not logs:
        print("⚠️ No logs to analyze.")
        return []

    # Expanded normal logs dataset (More diverse & realistic)
    normal_logs = [
        "INFO: Application started", "DEBUG: Database connected", "INFO: Request processed",
        "INFO: Health check passed", "DEBUG: Configuration loaded", "INFO: User logged in",
        "INFO: Cache refreshed", "INFO: Security check complete", "DEBUG: Load balancer updated",
        "INFO: Job execution completed", "INFO: Service restarted", "DEBUG: Connection established",
        "INFO: Scheduled job executed", "INFO: API request successful", "DEBUG: Memory usage normal",
        "INFO: Disk cleanup process completed", "INFO: Background job completed",
        "INFO: Configuration reloaded successfully", "INFO: Authentication successful",
        "DEBUG: No issues found in audit logs"
    ]
    
    # Train the model only if it doesn’t exist or needs an update
    if not os.path.exists(model_file) or len(normal_logs) > 15:
        print("🔄 Training optimized anomaly detection model with diverse normal logs...")
        normal_features = extract_features(normal_logs)
        model = IsolationForest(contamination=0.08, random_state=42)  # Lower threshold for anomalies
        model.fit(normal_features)
        joblib.dump(model, model_file)
        print("✅ Improved model trained and saved.")

    # Load the trained model and detect anomalies
    model = joblib.load(model_file)
    log_features = extract_features(logs)
    anomaly_predictions = model.predict(log_features)

    anomalies = [logs[i] for i in range(len(logs)) if anomaly_predictions[i] == -1]
    
    with open(anomaly_log_file, "w", encoding="utf-8") as f:
        f.write("\n".join(anomalies))

    if anomalies:
        print(f"⚠️ {len(anomalies)} anomalies detected and saved in: {anomaly_log_file}")
    else:
        print("✅ No anomalies detected.")

    return anomalies

if __name__ == "__main__":
    print("🚀 Log filtering & AI anomaly detection started...")

    # Step 1: Filter logs
    filtered_logs = filter_logs(log_file_path, log_levels_to_filter, filtered_log_file)

    # Step 2: Apply AI-based anomaly detection
    detect_anomalies(filtered_logs)

    print("✅ Process completed successfully!")
