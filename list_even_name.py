'''Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#numList=[]

def even_number_list(list):
    #for i in a:
        #if (i%2 )==0 :
         #   numList.append(i)'''
    numList = [element for element in a if element % 2 == 0]
    print (numList)

#x=lambda a: a % 2 == 0
#print(x(a))

even_number_list(a)



