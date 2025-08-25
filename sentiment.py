import pandas as pd
import requests

# Hugging Face API setup
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = "" #replace with your authentication

# Function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Function to analyze sentiment for a given text
def analyze_sentiment(text):
    try:
        # Make a request to the Hugging Face API to get sentiment analysis
        response = query({"inputs": text})
        if isinstance(response, list) and len(response) > 0:
            # Extract the sentiment with the highest score
            sentiment = max(response[0], key=lambda x: x['score'])
            return sentiment['label'], sentiment['score']
        else:
            return "Error", 0
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return "Error", 0

# Load the spreadsheet (replace with the path to your file)
file_path = ""
df = pd.read_excel(file_path)

# Ensure the column name matches the one in your file
text_column = "text_translated"  # The column containing translated text

# Remove NaN or empty values from the text column
df = df[df[text_column].notna() & (df[text_column] != '')]

# Apply sentiment analysis to the non-empty rows
print("Performing sentiment analysis. This might take a while...")
df[['Sentiment', 'Score']] = df[text_column].apply(lambda x: pd.Series(analyze_sentiment(x)))

# Save the result to a new spreadsheet
output_file_path = "/Users/prabhpreet16/Downloads/bjptweets/bjptweets_sentiment.xlsx"
df.to_excel(output_file_path, index=False)

print(f"Sentiment analysis completed. Results saved to {output_file_path}")
