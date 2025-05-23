import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

# Load your tweet data
df = pd.read_csv("elonmusk_tweets.csv")  # Make sure this file exists in the correct location

# Handle any missing data
df['tweet_text'] = df['tweet_text'].fillna("")

# Function to calculate sentiment polarity
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity  # -1 to +1

# Apply sentiment analysis
df['sentiment'] = df['tweet_text'].apply(get_sentiment)

# Label the sentiment
df['sentiment_label'] = df['sentiment'].apply(
    lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral')
)

# Plot the sentiment distribution
sns.countplot(x='sentiment_label', data=df, palette='Set2')
plt.title('Sentiment Distribution of Elon Musk Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Tweet Count')
plt.show()

