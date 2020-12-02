#1Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re
text= input("Enter the text: ")
result=re.sub("[A-Za-z0-9"], '', text)
if len(result) == 0:
print("Yes!It contains only alphabets and numbers")
else:
print("No it contains other than alphabets and numbers")

**************************************************************************************

#2Write a Python program that matches a word containing 'ab'.

import re
def check(text):
        patterns = '\a*b.\a*'
        if re.search(patterns,  text):
                return 'Yes!! a and b are found in the text'
        else:
                return('No!! a and b are not found in the text')

print(check("A boy is playing with a ball"))
print(check("Python10 Exercises."))

*******************************************************************************************

#3Write a Python program to check for a number at the end of a word/sentence.
import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return 'Yes!Number is present at the end of string'
    else:
        return 'No!Number is not present at the end of string'

print(end_num('Raja4098'))
print(end_num('Raja'))

*********************************************************************************************


#4Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

import re
list= re.finditer(r"([0-9]{1,3})", "These are the numberss 1, 12, 13,12,13 and 345")
print("The Numbers of length 1 to 3 are")
for n in list:
     print(n.group(1))
     
************************************************************************************************

#5 Write a Python program to match a string that contains only uppercase letters

import re 


def match(text): 
		
		
		pattern = '[A-Z]+$'
		
		if re.search(pattern, text): 
				return('Yes! it contains only upper case') 
		else: 
				return('No! It does not not contain upper case only') 

# Driver Function 
print(match("RAJA"))
print(match("RajaDhananjeyan")) 
print(match("raja"))

 


