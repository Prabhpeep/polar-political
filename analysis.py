import pandas as pd

# Load the spreadsheet 
file_path = "/replace_with_your_file_path"
df = pd.read_excel(file_path)

# Ensure the column name matches your file
sentiment_column = "Sentiment"

# Define the words to count
words_to_count = ["neutral", "positive", "negative"]

# Count occurrences of each word
word_counts = {word: (df[sentiment_column].str.lower() == word).sum() for word in words_to_count}

# Print the counts
print("Sentiment Counts:")
for word, count in word_counts.items():
    print(f"{word.capitalize()}: {count}")
