'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

'''

num1 = int(input("Please enter the no to which you need to divide :  "))

xlist=list(range(1,num1+1))
list1=[]
for num in xlist:
    if(num1%num)==0:
        list1.append(num)


print(list1)


