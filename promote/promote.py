import tweepy
import time
import os
import random

def post_tweets():
    client = tweepy.Client(
        consumer_key=os.environ["API_KEY"],
        consumer_secret=os.environ["API_SECRET"],
        access_token=os.environ["ACCESS_TOKEN"],
        access_token_secret=os.environ["ACCESS_SECRET"]
    )
    
    messages = [
        "Join our revolutionary project!",
        "Huge gains ahead! $TOKEN",
        "Limited time opportunity!"
    ]
    
    while True:
        message = random.choice(messages)
        client.create_tweet(text=message)
        time.sleep(random.randint(300, 900))

if __name__ == "__main__":
    post_tweets()
