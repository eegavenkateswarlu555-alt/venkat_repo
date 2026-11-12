# 1. check whether two Boolean variables are both True using and?
# a = True
# b = True

# result = a and b
# print("both are true : ", result)
# print("both are not true : ", not result)

# 2. check whether at least one of two Boolean variables is True using or?
# a = True
# b = False

# print("value a : ", a)
# print("value b : ", b)

# result = a or b
# print("at least one is true : ", result)

# 3. to reverse a Boolean value using not?
# value = input("enter a boolean value (True/False) : ")
# value = value = True
# print("Reversed value : ", not value)

# 4. to check whether a person's age is at least 18 and at most 60?
# age = int(input("Enter your age : "))
# print("Is age between 18 and 60 ? :", age >=18 and age <=60)

# 5. to check whether a number is greater than 10 and less than 100?
# number = int(input("Enter your number :"))
# print("Is number between 10 and 100 ? : ", number >=10 and number <=100)

# 6.  check whether a number is divisible by both 3 and 5?
# number = int(input("Enter your number : "))
# print("Is number is divisible by both 3 and 5 ? : ", number % 3==0 and number % 5==0)

# 7. to check whether a number is divisible by either 2 or 7?
# number = int(input("Enter a number :"))
# print("Is number is divisible by either 2 or 7 ? :",number % 2==0 or number % 7==0)

# 8. whether a student passed both Mathematics and Science, assuming the pass mark is 35 in each subject?
# enter both subject marks
# math_marks = int(input("Enter student (math_marks) : "))
# science_marks = int(input("Enter student (science_marks) :"))

# check whether student passed both subjects
# print("Student passed both subjects : ", math_marks >=35 and science_marks >=35)

# 9. whether a person is eligible to vote if their age is at least 18 and they are a citizen?
# age = int(input("Enter person age : "))
# is_citizen = bool(input("Enter the citizenship status (True or False) : "))

# print("you are eligible to vote :",age >=18)

# 10. to check whether both the entered username and password match the expected values?
# username = str(input("Enter user name :"))
# password = str(input("Enter password : "))

# correct_username = "venkat"
# correct_password = "venky@123"

# print("Login successful (when user has expeted both the values): ",
#       username == correct_username and password == correct_password)

# 11. to check whether a number is outside the range of 10 to 50 using not?
# number = int(input("Enter a range of number : "))
# Is_outside = not(10<= number<=50)
# print("Is the number outside range 10 to 50 ? :",Is_outside)

# 12. to check whether a character is not a lowercase vowel?
# character = input("Enter a character: ")

# is_not_lowercase_vowel = character not in "aeiou"

# print("Is the character not a lowercase vowel?", is_not_lowercase_vowel)

# 13. to check whether a number is positive and even?
# number = int(input("Enter an integer : "))
# Is_positive = number > 0
# Is_even = number % 2 == 0
# print("The number positive and even : ", Is_positive and Is_even)

# 14. to check whether a number is negative or equal to zero?
# number = int(input("Enter a number : "))
# print("The number is negative or equal to zero : ",number < 0 or number == 0)

# 15. student qualifies if their marks are at least 40 or their attendance is at least 90%?
# marks = float(input("Enter marks : "))
# attendance = float(input("Enter attendance percentage: "))
# student_qualifies = marks >= 40 or attendance <=90
# print("Studnet qualify : ",student_qualifies)

# 16. check whether a person qualifies for a discount if they are a senior citizen or a loyalty-program member?
# Is_senior = bool(input("Enter the Senior-citizen status (True or False) : "))
# Is_member = bool(input("Enter the membership status (True or False) : "))
# qualify_discount = Is_senior or Is_member

# print("you qualify for a discount : ",qualify_discount)

# 17. to check whether a year is between 2000 and 2026, inclusive?
# year = int(input("Enter a year : "))
# Is_year = year <= 2000 and 2026
# print("The year is between 2000 and 2026 : ",Is_year)

# 18. to check whether a number is not divisible by 2 using not?
# number = int(input("Enter a number : "))
# print("check if number is divisible or not : ", not number % 2==0)

# 19. to check whether a person can enter an event if their age is at least 18 and they have a valid ticket?
# age = int(input("Enter the age : "))
# ticket_info= input("please enter the ticket :  (yes or no) ")
# ticket_validation = ticket_info == "yes"
# Is_person_enter = age >=18 and ticket_validation

# if Is_person_enter:
#     print("Welcome! you can enter an event :",Is_person_enter)

# else :
#     print("Access Denied ! your age should at least 18 years old and you have a valid tciket : ",Is_person_enter)




# 20. to check whether a number is greater than 0, less than 100, and not equal to 50?
# number = int(input("Enter a number : "))
# Is_number = number >0 and number <100 and number!=50
# print("check the stauts : ",Is_number)







































