import pandas as pd
import re

# Load the dataset
df = pd.read_csv("elonmusk_tweets.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove missing values
df.dropna(inplace=True)

# Clean tweet text (remove links, special characters, extra spaces)
def clean_text(text):
    text = re.sub(r"http\S+|www\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z0-9\s.,!?]", "", text)  # Keep only text, numbers, and punctuation
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text.lower()  # Convert to lowercase

df["tweet_text"] = df["tweet_text"].apply(clean_text)

# Save cleaned data
cleaned_csv_filename = "elonmusk_tweets_cleaned.csv"
df.to_csv(cleaned_csv_filename, index=False)

print(f"Cleaned data saved to '{cleaned_csv_filename}'")
