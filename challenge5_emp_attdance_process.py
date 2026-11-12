# CHALLENGE 5: EMPLOYEE ATTENDANCE PROCESSING

# 1. Find employees present on both days.

# day_1 = {101, 102, 103, 104, 105}
# day_2 = {103, 104, 105, 106, 107}

# present_both_days=day_1 & day_2
# print("Present both days : ",present_both_days)

# # 2. Find employees absent on the second day from those who attended the first day.
# day_1 = {101, 102, 103, 104, 105}
# day_2 = {103, 104, 105, 106, 107}
# absent_second_day=day_1 - day_2
# print("absent second day : ",absent_second_day)

# # 3. Find all employees who attended at least one day.
# day_1 = {101, 102, 103, 104, 105}
# day_2 = {103, 104, 105, 106, 107}

# all_employees = day_1 | day_2
# print("employees who attended at least one day : ",all_employees)

# The | operator combines both sets without duplicates.

# Expected Output:
# Present Both Days = {103, 104, 105}
# Absent On Second Day = {101, 102}
# Attended At Least One Day = {101, 102, 103, 104, 105, 106, 107}
