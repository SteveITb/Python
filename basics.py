#Python Basics
"""
Python Basics
(Multiline comment)
"""

'''
Python Basics
'''

#integer
num1=10
num2=20

sum=num1+num2
price=200.50
name="John"
age=20
print(sum) #30
print("The sum is", sum)
print(f"The sum is {sum}")
print(f"The sum is {price:.3f}")
print(f"{name} is {age} years old")
print(name +  "is" + str(age) + "years old")

#printing to a file, open(path,mode- r,w,a)


f= open("C:\\Users\\ADMIN\\basics.txt", "w")
#integer
num1=10
num2=20

sum=num1+num2
print("The sum is", sum file=f)
f.close()

#floating point numbers
pi=3.142

print("The price is", price)

#string
name="John"

#Boolean
tall=True
