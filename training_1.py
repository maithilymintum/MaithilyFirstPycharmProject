#demo1
#excercise 1  Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

"""name=input("Please enter your name -")
age= float(input("Please enter your Age -"))
num = int(input("Enter the no of time you nee it printed"))

age_1=100-age
i= 0

while i < num:
    i += 1
    print("Hi " + name + " you have ",age_1 ,"years to complete a century!\n")
   # print(num)
"""

#Excercise 2 - Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.



#number=int(input("Please enter the no whcih needs to validated -"))

#sub= number%2

#if sub ==1:
 #   print("the no you have entered is Odd")
#else:
 #   print("the no is even!")

#rem = number%4
#if rem ==0:
#   print("the no is a multiple of 4")



num1 = int(input("Please enter the no to which you need to divide :  "))
check = int(input("Please Enter the no by which you need to divide : "))

#sub=num1%check

if (num1%check)==0:
    print("Both no are multiple of each other")
else:
    print("the no are not related to each other")


