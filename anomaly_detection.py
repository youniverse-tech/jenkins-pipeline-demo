import requests

# Slack Webhook URL (Replace with your actual Webhook URL)
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

def send_slack_alert(message):
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if response.status_code == 200:
        print("✅ Slack alert sent successfully!")
    else:
        print(f"❌ Failed to send Slack alert. Error: {response.text}")

# Example usage - Call this function when an anomaly is detected
send_slack_alert("🚨 *Alert!* An anomaly (ERROR/WARNING) was detected in the logs.")

