import praw
import os
from dotenv import load_dotenv

load_dotenv()
client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")
user_agent = os.environ.get("user_agent")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
)
print(reddit)
