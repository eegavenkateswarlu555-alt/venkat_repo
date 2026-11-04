## DE-131: Extract Source System Name
# Extract the first four characters from the source system identifier.

# source_name = "DATAENGINEER"
# first_four_characters = source_name[0:4]
# print("First Four Characters : ",first_four_characters)

## DE-132: Extract Customer ID Suffix
# Extract the last four characters from the customer identifier.

# customer_id = "CUSTOMER1025"
# Last_Four_Characters = customer_id[-4:]
# print(Last_Four_Characters)

## DE-133: Extract Transaction Year
# Extract the year from the transaction date.

# transaction_date = "2026-11-02"
# year = transaction_date[0:4]
# print("Year : ",year)

## DE-134: Extract Transaction Month
# Extract the month from the transaction date.

# transaction_date = "2026-11-02"
# month = transaction_date[5:7]
# print("Month : ",month)

## DE-135: Extract Transaction Day
# Extract the day from the transaction date.

# transaction_date = "2026-11-02"
# day = transaction_date[8:10]
# print("day : ",day)

## DE-136: Extract Filename Without Extension
# Extract the filename without its CSV extension.

# file_name = "employees.csv"
# filename_without_extension = file_name[:-4]
# print("Filename without extension: ", filename_without_extension)
# print("Filename without extension: ", file_name[0:len(file_name)-4])

## DE-137: Reverse Transaction Identifier
# Reverse the transaction identifier using string slicing.

# transaction_id = "TXN12345"
# reversed_transaction_id = transaction_id[::-1]
# print("Reversed Transaction ID: ", reversed_transaction_id)

## DE-138: Extract Alternate Characters
# Extract alternate characters from the source system identifier, starting from index zero.

# source_id = "ABCDEFGHIJ"
# alternate_characters = source_id[0::2]
# print(alternate_characters)

## DE-139: Extract Date from Pipeline Logs
# Extract the date portion from a fixed-format pipeline error message.

# log_message = "ERROR|20261102|CUSTOMER_ETL"
# date_portion = log_message.split("|")[1]
# print(date_portion)

## DE-140: Extract Transaction ID Components
# Extract the transaction prefix, year and sequence number from a fixed-format transaction identifier.

# transaction_id = "TXN-2026-1001"
# item_parts = transaction_id.split("-")
# item_prefix = item_parts[0]
# item_year = item_parts[1]
# item_sequence = item_parts[2]

# print("Item prefix : ",item_prefix)
# print("Item year   : ",item_year)
# print("Item sequence : ",item_sequence)



