from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>", level="INFO")


# Challenge 1: Messy Price to Float
# Convert a scraped string like "R$ 1.250,99" or "US$ 1,250.99" into a clean Python float (1250.99).
values = "US$ 1,250.99"
values = values.replace("US$ ", "").replace(",", "")
values = float(values)
logger.info(f"Challenge 1: {values}")



# Challenge 2: Phone Number Formatting
# Extract a phone number from a messy text block and format it strictly to (XX) XXXXX-XXXX.
phone_number = "Contact us at +55 (11) 91234-5678 or email support."
number = ''.join(filter(str.isdigit, phone_number))
formatted_number= f"({number[2:4]}) {number[4:9]}-{number[9:]}"
logger.info(f"Challenge 2: {formatted_number}")

# Challenge 3: HTML Tag Stripping
# Remove all HTML tags, CSS classes, and non-breaking spaces (&nbsp;) from a scraped paragraph, returning only clean plain text.



# Challenge 4: Email Extraction
# Extract the first valid email address from a block of unstructured text using Regex.



# Challenge 5: Company Name Normalization
# Clean a string that has trailing/leading spaces, multiple internal spaces, and weird characters (e.g., "  ACME   Corp. & Co.!! " -> "ACME Corp. & Co.").



# Challenge 6: Text Date to ISO
# Convert a scraped string like "25 de Outubro de 2023" to standard ISO format "2023-10-25".



# Challenge 7: Days Difference
# Calculate the exact difference in days between a scraped date string and today's date.



# Challenge 8: Unix Timestamp Conversion
# Convert a Unix timestamp (e.g., 1698249600) from an API response to a human-readable "DD/MM/YYYY HH:MM" string.



# Challenge 9: Multi-Format Date Parser
# Parse a date string that might be in multiple formats (e.g., "2023-10-25", "25/10/2023", or "Oct 25, 2023") and standardize it to YYYY-MM-DD.

# Challenge 10: Datetime Slicing
# Extract just the year and month from a full ISO datetime string like "2023-10-25T14:30:00Z" and return "2023-10".

# Challenge 11: Percentage to Decimal
# Convert a percentage string like "12,5%" to a decimal float 0.125.

# Challenge 12: Extract Numeric Value
# Extract the numeric value from a string like "Total: 1,250.00 USD" and convert it to a float.

# Challenge 13: Float to BRL Currency
# Format a float 1250.99 into a Brazilian currency string "R$ 1.250,99".

# Challenge 14: K/M Suffix Conversion
# Convert a string representing thousands/millions (e.g., "1.5M" or "2.3K") to an actual integer (1500000 or 2300).

# Challenge 15: Null Value Handling
# Handle a scraped value that might be "N/A", "-", "--", or an empty string, and deterministically return "NO_DATA" or None.

# Challenge 16: Tuples to JSON
# Convert a list of tuples [('name', 'John'), ('age', '30')] into a properly formatted JSON string.

# Challenge 17: Flatten Nested Dict
# Flatten a nested dictionary {'user': {'name': 'John', 'address': {'city': 'NY'}}} into a single-level dictionary {'user_name': 'John', 'user_address_city': 'NY'}.

# Challenge 18: Deep Key Extraction
# Extract a specific key-value pair from a complex, messy JSON string where the key might be nested at an unknown depth.

# Challenge 19: CSV String to Dicts
# Convert a raw CSV string (which includes commas inside quoted values) into a list of dictionaries.

# Challenge 20: Dict Merge (Left Join)
# Merge two lists of dictionaries based on a common key (e.g., 'id'), keeping all records from the first list even if there is no match in the second.

# Challenge 21: URL Slug Generation
# Remove all accents and special characters from a string (e.g., "São Paulo & Rio!" -> "Sao-Paulo-e-Rio") for safe URL generation.

# Challenge 22: URL Deduplication
# Extract all URLs from a block of text and return them as a deduplicated list, removing trailing slashes.

# Challenge 23: Data Masking (LGPD/GDPR)
# Mask sensitive data in a string (e.g., replace the middle digits of a CPF "123.456.789-00" with "XXX.XXX.789-00").

# Challenge 24: Multi-Separator Email Parser
# Parse a string containing multiple email addresses separated by commas, semicolons, or newlines, and return a clean, stripped list.

# Challenge 25: CNPJ Validation
# Validate if a string is a valid Brazilian CNPJ (14 digits, correct format, and valid check digits) and return True or False.