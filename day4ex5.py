Exercise:
1)Create a function getting two integer inputs from user. & print the following:

Addition of two numbers is +value
Subtraction of two numbers is +value
Division of two numbers is +value
Multiplication of two numbers is +value

Here the value represents math function associated


            2. Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree
						
						#EXERCISE1
						PROGRAM
						def arith_ope(a,b):
						print("Sum of two numbers is:" ,a+b)
					  print("Differnce of two numbers is:" ,a-b)
						print("Multiplication of two numbers is:" ,a*b)
						print("Divisiom of two numbers is:" ,a/b)
					  x=int(input("Enter the first number:"))
						y=int(input("Enter the second number:"))
						arith_ope(x,y)
						
						OUTPUT:
						Enter the first number:100
            Enter the second number:50
            Sum of two numbers is: 150
            Differnce of two numbers is: 50
            Multiplication of two numbers is: 5000
            Divisiom of two numbers is: 2.0
						
						
						#EXERCISE 2
						PROGRAM
						def covid(name,temp=98):
            print("Patient name : ",name)
            print("Body Temperature : ",temp)
            a = input("Enter patient name: ")
            covid(a)
						
						OUTPUT:
						Enter patient name: Dhananjeyan
            Patient name :  Dhananjeyan
            Body Temperature :  98
						
						
