import os
from slack import WebClient
from slack.errors import SlackApiError
from htmldate import find_date

# Get Slack token from environment variable
slack_token = os.environ.get('SLACK_API_TOKEN')

# Initialize Slack client
client = WebClient(token=slack_token)

# List of URLs to process
urls = [
    "https://today.umd.edu/umd-launches-institute-focused-on-ethical-ai-development",
    "https://www.trails.umd.edu/",
    "https://artiamas.umd.edu/",
    "https://ml.umd.edu/",
    "http://www.cfar.umd.edu/",
    "http://www.umiacs.umd.edu/"
]

# Prepare message with publication dates
msg = "*Website Last Modified Dates:*\n"
for url in urls:
    date = find_date(url)  # Extract publication date
    msg += f"• <{url}|{url}>: {date if date else 'Unknown'}\n"  # Format message for Slack

# Send message to Slack
try:
    response = client.chat_postMessage(
        channel="slack-bots",
        text=msg,
        unfurl_links=True,
        unfurl_media=True
    )
    print("Success! Message sent to Slack.")
except SlackApiError as e:
    print(f"Got an error: {e.response['error']}")
