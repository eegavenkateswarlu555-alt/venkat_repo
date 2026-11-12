# CHALLENGE 2: CUSTOMER DATA DEDUPLICATION

# 1. Combine both customer ID lists.
# branch_1 = [101, 102, 103, 104, 105]
# branch_2 = [103, 104, 106, 107, 108]

# all_customer_ids=set(branch_1 +branch_2)
# print(all_customer_ids)

# # 2. Remove duplicate IDs using sets.
# duplicate_Ids=set(branch_1) & set(branch_2)
# print(duplicate_Ids)

# # 3. Find common customer IDs.
# common_Ids=set(branch_1) & set(branch_2)
# print(common_Ids)

# # 4. Display all unique customer IDs.
# branch_1 = [101, 102, 103, 104, 105]
# branch_2 = [103, 104, 106, 107, 108]


# unique_Ids = set(branch_1) | set(branch_2)
# print("All customer unique Ids : ",unique_Ids)
# print("Total unique customer Ids : ",len(unique_Ids))

# Expected Output:
# All Customer IDs = {101, 102, 103, 104, 105, 106, 107, 108}
# Common Customer IDs = {103, 104}
# Total Unique Customers = 8