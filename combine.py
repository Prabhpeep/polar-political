import pandas as pd
import os

# Folder containing the 21 spreadsheets
input_folder = "/"  # Replace with the path to your folder
output_file = "/"  # Path to save the final combined file

def combine_spreadsheets(input_folder, output_file):
    # List all Excel files, ignoring temporary files starting with '~$'
    excel_files = [
        file for file in os.listdir(input_folder)
        if (file.endswith(".xlsx") or file.endswith(".xls")) and not file.startswith("~$")
    ]
    

    if len(excel_files) != 21:
        print(f"Warning: Found {len(excel_files)} Excel files instead of 21.")
    
    combined_df = pd.DataFrame()  # Initialize an empty DataFrame
    
    # Loop through each Excel file and append it to the combined DataFrame
    for file in excel_files:
        file_path = os.path.join(input_folder, file)
        print(f"Reading file: {file_path}")
        try:
            df = pd.read_excel(file_path)  # Read the Excel file
            combined_df = pd.concat([combined_df, df], ignore_index=True)  # Append to the combined DataFrame
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
    
    # Save the combined DataFrame to a new Excel file
    combined_df.to_excel(output_file, index=False)
    print(f"Combined file saved to: {output_file}")

if __name__ == "__main__":
    combine_spreadsheets(input_folder, output_file)
