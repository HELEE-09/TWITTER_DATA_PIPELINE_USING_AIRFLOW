from textblob import TextBlob
import pandas as pd

# Load tweets
df = pd.read_csv("elonmusk_tweets.csv")

# Function to get sentiment
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity  # -1 to 1

# Apply sentiment to each tweet
df['sentiment'] = df['tweet_text'].dropna().apply(get_sentiment)

# Classify as positive, negative, or neutral
df['sentiment_label'] = df['sentiment'].apply(
    lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral')
)

# Count sentiment categories
print(df['sentiment_label'].value_counts())
