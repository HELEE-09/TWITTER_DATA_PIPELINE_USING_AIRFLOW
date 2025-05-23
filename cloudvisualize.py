import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the CSV file (adjust path or use S3 path if needed)
df = pd.read_csv("s3://helee-airflow-youtube-bucket/elonmusk_tweets.csv")  # or use s3://... if s3fs is set up

# Combine all tweet text into one string
text = " ".join(tweet for tweet in df['tweet_text'].dropna())

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Elon Musk Tweets")
plt.show()
