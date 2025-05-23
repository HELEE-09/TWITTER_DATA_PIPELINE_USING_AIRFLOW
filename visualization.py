import pandas as pd
import matplotlib.pyplot as plt

# Load from S3 (make sure s3fs is installed and AWS keys are set)
df = pd.read_csv("s3://helee-airflow-youtube-bucket/elonmusk_tweets.csv")

# Convert time column to datetime
df['created_at'] = pd.to_datetime(df['created_at'])

# Plot tweet frequency
df.set_index('created_at').resample('h').size().plot(kind='bar')
plt.title('Tweet Frequency by Hour')
plt.xlabel('Time')
plt.ylabel('Tweet Count')
plt.show()
