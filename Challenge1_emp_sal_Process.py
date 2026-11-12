# Tasks:
# 1. Calculate total employee salary.
# 2. Calculate average salary.
# 3. Find employees earning above ₹40,000.
# 4. Store their names in a separate list.
# Given the following employee records:
# employees = [
#     {"name": "Rahul", "salary": 35000},
#     {"name": "Anil", "salary": 50000},
#     {"name": "Kiran", "salary": 45000},
#     {"name": "Arun", "salary": 30000}
# ]
# total = 0
# for items in employees:
#     total += items["salary"]

# print("Total Salary : ",total)    
# # TypeError: unsupported operand type(s) for +: 'int' and 'dict'

# # 2. Calculate average salary.
# average_salary=total/len(employees)
# print(average_salary)

# # 3. Find employees earning above ₹40,000.
# for employee in employees:
#     if employee["salary"] > 40000:
#         print(employee["name"], employee["salary"])

# # 4. Store their names in a separate list.
# names = []
# for employee in employees:
#     if employee["salary"] > 40000:
#         names.append(employee["name"])

# print(names)

