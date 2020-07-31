import json
import requests

slack_webhook = "https://hooks.slack.com/services/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"

def send_slack(event, context):
    """sends a slack message when triggered"""
    print(str(event))
    print("Sending slack message")
    slack_msg = {"text": "Message from py script"}
    resp = requests.post(slack_webhook, data=json.dumps(slack_msg))
    return resp.text

send_slack("event_name", "some context")