'''Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

#define an array -

list=[1,2,34,55,44,33,21,3,5,6,77,88,88,875,543]
xlist=[]

for element in list:
    if element<=5:
          xlist.append(element)

for ele in xlist:
    print(ele)
