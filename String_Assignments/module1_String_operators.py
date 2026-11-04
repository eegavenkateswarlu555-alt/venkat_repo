## DE-101: Clean Employee Name
# Remove the unwanted spaces and display the cleaned name.

# employee_name = "   VENKAT REDDY   "
# cleaned_name=employee_name.strip()
# print(cleaned_name)

## DE-102: Standardize Customer Email
#Convert the customer email address into lowercase before storing it in the database.

# email = "VENKAT@GMAIL.COM"
# print(email.lower())

## DE-103: Standardize Employee Name
# Convert the employee name so that the first character of each word is uppercase.
# import string
# employee_name = "venkat reddy"
# formatted_text = string.capwords(employee_name)
# print(formatted_text)

## DE-104: Standardize File Name
#Replace spaces in an incoming data file name with underscores.
# file_name = "employee data november.csv"
# clean_filename = file_name.replace(" ","_")
# print(clean_filename)

## DE-105: Identify CSV File Extension

#Check whether an incoming file name ends with the CSV extension.
# file_name = "employees.csv"
# print(file_name.endswith("csv"))

## DE-106: Extract Customer Email Domain
# Extract the email provider domain from the customer email address.
# email = "venkat@gmail.com"
# # split at @ and grab the second part
# domain = email.split("@")[1]
# print(domain)

## DE-107: Standardize Transaction Status
# Convert the transaction status into uppercase before generating a transaction report.

# status = "success"
# transaction_report = status.upper()
# print(transaction_report)

## DE-108: Clean Customer Location
# Remove unwanted spaces from the customer location.

#location = "     Bangalore     "
# cleaned_name = location.strip()
# print(cleaned_name)

## DE-109: Validate Numeric Employee ID
# Check whether the employee ID contains only numeric characters.

# employee_id = "102345"
# final_Id = employee_id.isnumeric()
# print("after final result is : ",final_Id)

## DE-110: Identify Employee ID Prefix
# Check whether the employee ID starts with the prefix EMP.

# employee_id = "EMP101"
# final_text = employee_id.startswith("EMP")
# print(final_text)


















