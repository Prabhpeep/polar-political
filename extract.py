import pandas as pd
import os

def extract_columns(input_file, output_file, columns_to_extract):
    """
    Reads a spreadsheet, extracts specific columns, and saves to a new file.

    Args:
        input_file (str): Path to the input spreadsheet.
        output_file (str): Path to save the new filtered spreadsheet.
        columns_to_extract (list): List of columns to extract.
    """
    try:
        # Check if file exists
        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' not found.")
            return
        
        # Read the spreadsheet
        print(f"Reading file: {input_file}")
        df = pd.read_excel(input_file)
        
        # Check if required columns exist
        missing_columns = [col for col in columns_to_extract if col not in df.columns]
        if missing_columns:
            print(f"Error: Missing columns: {missing_columns}")
            return
        
        # Extract specific columns
        filtered_df = df[columns_to_extract]
        
        # Save the filtered DataFrame to a new file
        print(f"Saving filtered data to: {output_file}")
        filtered_df.to_excel(output_file, index=False)
        
        print("Extraction complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input file path (adjust this to your file location)
    input_file = "/"
    # Output file path
    output_file = "/"
    # Columns to extract
    columns_to_extract = ["mainTweetUrl", "text", "likes", "replies"]
    
    # Run the extraction function
    extract_columns(input_file, output_file, columns_to_extract)
