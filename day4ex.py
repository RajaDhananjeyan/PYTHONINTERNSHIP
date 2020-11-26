Exercise:
1.Write a program to create a list of n integer values and do the following
Add an item in to the list (using function)
Delete (using function)
Store the largest number from the list to a variable
Store the Smallest number from the list to a variable

     2) Create a tuple and print the reverse of the created tuple
     3) Create a tuple and convert tuple into list


#EXERCISE1
a=['apple','banana','pear','papaya']
a.append('mango')    #ADDING AN ITEM TO THE LIST
print(a)

a.remove('pear)    #REMOVING AN ITEM TO THE LIST
print(a)


a=[12,13,23,25,32,11,10]
a.sort()
print("Largest item of the list is" a[-1])   #FINDING THE LARGEST ITEM OF THE LIST
print("Largest item of the list is" a[0])    #FINDING THE SMALLEST ITEM OF THE LIST



#EXERCISE2
a=[10,15,16,17,25,23]
b=reversed(a)
print(tuple(b))


#EXERCISE3
a=['apple','pear','banana','papaya']
b=list(a)
print(b)
