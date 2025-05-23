import tweepy
import pandas as pd
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def run_twitter_etl():  # Function definition
    """Extracts Elon Musk's tweets and saves them as a CSV."""

    # Twitter authentication
    client = tweepy.Client(
        bearer_token=os.getenv("BEARER_TOKEN"),
        consumer_key=os.getenv("API_KEY"),
        consumer_secret=os.getenv("API_SECRET_KEY"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

    time.sleep(120)  # Delay for rate limits (optional)

    # Fetch recent tweets (extract data)
    response = client.get_users_tweets(
        id='44196397',  # Elon Musk's Twitter ID
        max_results=10,  # Limited to 10 tweets
        tweet_fields=['created_at', 'text']
    )

    if response.data:
        # Process tweets
        data = [{"created_at": tweet.created_at, "tweet_text": tweet.text} for tweet in response.data]

        # Convert to CSV
        df = pd.DataFrame(data)
        csv_filename = "s3://helee-airflow-youtube-bucket/elonmusk_tweets.csv"
        df.to_csv(csv_filename, index=False)

        print(f"Data successfully saved to '{csv_filename}'")
    else:
        print("No tweets found.")


# Run the ETL function
run_twitter_etl()

