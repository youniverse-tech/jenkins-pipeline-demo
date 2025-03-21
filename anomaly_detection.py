import requests

# Slack Webhook URL (Replace this with your actual Slack Webhook URL)
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

def send_slack_alert(message):
    """
    Sends an alert message to Slack using the webhook.
    """
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        print("✅ Slack alert sent successfully!")
    else:
        print(f"❌ Failed to send Slack alert. Error: {response.text}")

def check_logs():
    """
    Reads the filtered logs file and sends an alert if anomalies (ERROR, WARNING, SEVERE) are found.
    """
    log_file = "filtered_logs.txt"

    try:
        with open(log_file, "r") as file:
            logs = file.readlines()

        anomalies = [log.strip() for log in logs if any(level in log for level in ["ERROR", "WARNING", "SEVERE"])]

        if anomalies:
            alert_message = "🚨 *Alert!* Anomalies detected in logs:\n" + "\n".join(anomalies)
            send_slack_alert(alert_message)
        else:
            print("✅ No anomalies found in logs.")

    except FileNotFoundError:
        print(f"❌ Log file '{log_file}' not found. Make sure Jenkins has generated logs.")

# Run the log check function
if __name__ == "__main__":
    check_logs()
