import os
import csv
from slack import WebClient
from slack.errors import SlackApiError
from htmldate import find_date
from datetime import datetime, timedelta
import dateutil.parser
import pytz

# Get Slack token from environment variable
slack_token = os.environ.get('SLACK_API_TOKEN')
client = WebClient(token=slack_token)

# Path to your CSV file containing URLs
csv_file_path = 'umd_institutes.csv'

# Get current time in Eastern Time
eastern = pytz.timezone('US/Eastern')
now = datetime.now(eastern)
one_day_ago = now - timedelta(days=1)

msg = "*Here are the University of Maryland research institution websites updated within the last 24 hours:*\n"
updates_found = False

# Read URLs from CSV
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        url = row['url']  # assuming the CSV has a column named 'url'
        if not url:
            continue
        try:
            # Attempt to extract the date of the webpage
            date_str = find_date(url)
            if date_str:
                # Parse the date
                date = dateutil.parser.parse(date_str)

                # Ensure the date is timezone-aware by converting it to Eastern Time
                if date.tzinfo is None:
                    date = eastern.localize(date)

                # Compare the website date with the current time (Eastern Time)
                if date > one_day_ago:
                    msg += f"• <{url}|{url}>: {date.date()}\n"
                    updates_found = True
            else:
                # If no date is found, log it
                print(f"⚠️ No date found for {url}")
        except Exception as e:
            # Handle any errors gracefully
            print(f"❌ Error processing {url}: {e}")

# If no updates were found, send a default message
if not updates_found:
    msg += "• No websites were updated in the last 24 hours."

# Send the message to Slack
try:
    response = client.chat_postMessage(
        channel="slack-bots",  # Replace with your actual Slack channel ID or name
        text=msg,
        unfurl_links=True,
        unfurl_media=True
    )
    print("✅ Message sent to Slack.")
except SlackApiError as e:
    print(f"❌ Slack API Error: {e.response['error']}")
