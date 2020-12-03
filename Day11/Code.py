#1 EXERCISE
list_1=[99198004098, 9918004009,9918004110, 9918004112, 9918004024]
list_2=["Dhananjeyan", "Badhri", "Anwar", "Siva", "Dheena"]
list_3=list_3 = list(zip(list_1, list_2))

print(list_3)

#2 EXERCISE

list_1=["RAJA", "BADHRI", "DHEENA", "ANWAR", "SIVA", "RAWNA", "DHANANJ","6GROUP"]
range = list(range(1,8))
lst = list(zip(list_1, range))
print(lst)


#3 EXERCISE

list= [98, 1, 53, 21, 4,65,2]
list.sort()
print("The sorted list is", list)


#4 EXERCISE

numbers= [1, 2, 4, 5, 7, 8, 10, 11]
def filterOddNum(num):
if(num % 2) == 0:
return False
else:
return True
oddfilter = filter(filterOddNum, numbers)
print("The odd numbers in the list are: ", list(oddfilter))
