import pandas as pd
import os

#=================== BASIC ===================

# Challenge 1: Create Directory Structure
# Create a Python script that automatically generates the following folder structure:
# /project
#   /input
#   /output
#   /processed
#   /errors
# The script should check if folders already exist before creating them.
def c1():
    os.makedirs("project/input", exist_ok=True)
    os.makedirs("project/output", exist_ok=True)
    os.makedirs("project/processed", exist_ok=True)
    os.makedirs("project/errors", exist_ok=True)



# Challenge 2: List Excel Files
# Create a function that receives a folder path and returns a list of all .xlsx files in that directory.
# Return an empty list if no Excel files are found.
def c2(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]




# Challenge 3: Read First Sheet
# Read the first sheet of an Excel file and display the first 5 rows in the console.
# Handle the error gracefully if the file doesn't exist.


# Challenge 4: Count Rows and Columns
# Create a function that receives an Excel file path and returns the number of rows and columns in the first sheet.
# Return (0, 0) if the file is empty.


# Challenge 5: Rename File with Date
# Create a function that renames an Excel file by appending today's date to the filename.
# Format: "filename_YYYYMMDD.xlsx"
# Example: "report.xlsx" -> "report_20261111.xlsx"


# Challenge 6: Copy All Excel Files
# Create a script that copies all .xlsx files from an "input" folder to a "backup" folder.
# Create the "backup" folder if it doesn't exist.


# Challenge 7: Read Specific Column
# Read only the "Client" column from an Excel file and display all unique values.
# Ignore null/NaN values.


# Challenge 8: Create New Spreadsheet
# Create a DataFrame with 3 columns (ID, Name, Value) and 5 rows of sample data, then save it to a new Excel file.
# Name the sheet "Data".


# Challenge 9: Move Old Files
# Create a script that moves all .xlsx files older than 7 days from an "input" folder to an "archive" folder.
# Use file modification date to determine age.


# Challenge 10: Check Empty File
# Create a function that checks if an Excel file is empty (no data rows) and returns True or False.
# Consider that headers don't count as data.


#=================== INTERMEDIATE ===================

# Challenge 11: Consolidate Multiple Sheets
# Read all .xlsx files from a folder and combine them into a single DataFrame.
# Add a column "Source" with the original filename for each row.
# Save the consolidated result to "consolidated.xlsx".


# Challenge 12: Filter Data by Condition
# Read an Excel file and filter all rows where the "Status" column equals "Pending".
# Save the filtered result to a new file.
# Create a parameterized function that accepts column name and value as arguments.


# Challenge 13: Batch Processing with Logging
# Create a script that processes all .xlsx files in a folder, reads the "Value" column, and calculates the total sum.
# Log each file: filename, row count, and sum.
# Handle corrupted files without breaking the loop.


# Challenge 14: Rename Columns
# Read an Excel file and rename columns based on a mapping dictionary.
# Example: {"client_name": "Client", "total_value": "Value"}
# Ignore columns that don't exist in the mapping.
# Save the result to a new file.


# Challenge 15: Split Sheet by Category
# Read an Excel file and split it into multiple files, one for each unique value in the "Category" column.
# Name the files as "category_X.xlsx" where X is the category value.
# Create an "output" folder to save the split files.


# Challenge 16: Merge Two Spreadsheets
# Read two different Excel files and perform a merge (join) based on a common column (e.g., "ID").
# Save the merged result to a new file.
# Handle cases where IDs don't match between files.


# Challenge 17: Remove Duplicate Rows
# Read an Excel file, remove all duplicate rows (considering all columns), and save to a new file.
# Log how many duplicate rows were removed.
# Keep the first occurrence of each duplicate.


# Challenge 18: Process Multiple Sheets
# Read all sheets from a single Excel file and combine them into one DataFrame.
# Add a column "Sheet" with the sheet name for each row.
# Use pd.read_excel(sheet_name=None) to read all sheets at once.


# Challenge 19: Validate Data Format
# Create a function that validates if all rows in an Excel file have the same number of columns.
# Return True if valid, False otherwise.
# Consider the first row as the header.


# Challenge 20: Incremental Backup
# Create a script that copies only .xlsx files modified in the last 24 hours from "input" to "backup".
# Log which files were copied and which were skipped.
# Create the backup folder if it doesn't exist.


#=================== ADVANCED ===================

# Challenge 21: Dynamic Column Extraction
# Create a function that accepts a list of column names and extracts only those columns from an Excel file.
# If a column doesn't exist, log a warning but continue processing.
# Save the filtered result to a new file.


# Challenge 22: Excel Formula Preservation
# Read an Excel file using openpyxl, modify specific cell values, and save while preserving all formulas.
# Ensure that calculated cells update correctly after modification.
# Handle merged cells without breaking the structure.


# Challenge 23: Multi-Level Aggregation
# Read an Excel file and perform groupby aggregation on multiple columns.
# Example: Group by "Region" and "Category", then calculate sum of "Value" and count of rows.
# Save the aggregated result with formatted column headers.


# Challenge 24: Conditional Formatting with OpenPyXL
# Read an Excel file and apply conditional formatting: highlight cells in the "Value" column where value > 1000 in red.
# Save the formatted file to a new location.
# Preserve existing formatting and styles.


# Challenge 25: Parallel File Processing
# Create a script that processes multiple Excel files concurrently using multiprocessing or threading.
# Each file should be read, filtered by a condition, and saved to an output folder.
# Implement proper error handling and logging for each parallel task.


# Challenge 26: Excel to JSON Conversion
# Read an Excel file and convert it to a JSON file where each row becomes a JSON object.
# Handle nested data structures if multiple sheets exist.
# Create a separate JSON file for each sheet, named after the sheet.


# Challenge 27: Data Validation Pipeline
# Create a validation pipeline that checks an Excel file for:
# - Missing required columns
# - Invalid data types (e.g., dates in text columns)
# - Out-of-range values
# Generate a validation report as a new Excel file with errors highlighted.


# Challenge 28: Recursive Folder Processing
# Create a script that recursively searches through nested folders for .xlsx files.
# Process each file found and save results to a corresponding output folder structure.
# Maintain the original folder hierarchy in the output.


# Challenge 29: Excel Template Generator
# Create a function that generates Excel files from a template with dynamic data injection.
# The template has placeholders like {{client_name}}, {{date}}, {{total_value}}.
# Read data from a source Excel file and generate multiple output files, one per row.


# Challenge 30: Automated Reporting System
# Build a complete reporting system that:
# - Reads multiple Excel files from different sources
# - Consolidates and transforms the data
# - Generates summary statistics and pivot tables
# - Creates a final report with multiple sheets (Summary, Details, Charts data)
# - Sends an email notification with the report attached (optional)
# - Logs all operations with timestamps and status
