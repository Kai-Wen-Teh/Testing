
"""
SECTION 1
name1 = input("Name: ")
name2= input("Another name: ")
print(name1, "has lost to", name2, "in the competition.")
"""

"""
SECTION 2
i = 0
while i < 10:
    print("The current index is", i)
    i += 1;
    
print("The last index is", i)

SECTION 3
x = 0
while x != 5:
    x = int(input("Enter the number 5 to end loop:"))


print("x should equal to", x, "right now.")


number1 = int(input("Enter an integer: "))
print("The factors are: ", end="")
for i in range(1, number1 + 1):
    if number1 % i == 0:
        if number1 == i:
            print(i)
        else:
            print(i, end=", ")
    

SECTION 4

def is_even(n):
    return n % 2 == 0

n = int(input("Enter: "))

print(n,"is even.") if is_even(n) else print(n, "is odd.")
            
SECTION 5
 
import random
def correctans(n1, n2, ans):
    return n1 * n2 == ans

x = 0
count = 0
score = 0
while x>= 0:
    print("Enter a negative number to quit.")
    a = random.randint(0, 12)
    b = random.randint(0, 12)
    count += 1
    x = int(input("Question " + str(count) + ": " + str(a) + " x " + str(b) + " = "))
    if correctans(a, b, x):
        score += 1
print("Your final score is:", score)

var = [1,'b',3.0]
var.pop(0)
print(var)
"""
# def addtwonumbers(a, b):
#     sums = a + b
#     return sums

# ans = 3
# print(addtwonumbers(1, ans))


# for i in range(0, 5, 1):
#     num = i * 2
#     print("The number is " + str(num) + ", you buffon.")

# haha = "python is very good yea Python 666"
# # print(haha.replace("very", '4'))
# print(haha.find('Python'))

# print (10)
# print('Hello World! \
# It might rain today. \
# Tomorrow is Sunday.')
# print('''Hello World!
# It might rain today.
# Tomorrow is Sunday.''')

# list1 = ["Bob", "Jack", "Grealish", "Bard"]
# print(list1[0:3])
# print(list1)

numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

for i in range(0, 5, 1): # 0 to 4 1st :initial value, 2nd: Final value(exclusive), 3rd: (increment)
    print(i * '*')
    
hahalist = (1,2,3,"happy", True, 2, 2) # Immutable tuples
print(hahalist.count(2))
        
    
table= [ [ 0 for i in range(3) ] for j in range(3) ]
print ("Enter values for a matrix of order 3 x 3")
for d1 in range(3):
  for d2 in range(3):
      table[d1][d2]= int(input())
print ("Elements of the matrix are", table)
print ("Elements of the matrix are")
for row in table:
    print (row)
s=0
for row in table:
    for n in row:
      s+=n
print ("The sum of elements in matrix is",s)

Tutorial 1
Question 1

a = input('Student ID: ')
b = input('Name: ')
c = input('Date of Birth: ')
d = int(input('Height(cm): '))
e = int(input('Weight(kg): '))
print('***Welcome to the Department of Electrical Engineering***')
print('Student ID: ',a)
print('Name: ',b)
print('Date of Birth: ',c)
print('Height(cm): ',d)
print('Weight(kg): ',e)

import math

print('Area Calculator for Basic Shapes')
print('================================')
print('1. Square')
print('2. Rectangle')
print('3. Triangle')
print('4. Circle')
s = int(input('Choose a shape[1-4] that you want calculate its area: '))
while s <= 0 or s > 4:
    s = int(input('Choose a shape[1-4] that you want calculate its area: '))

def area(i):
    if i == 1:
        l = float(input('Enter Length: '))
        b = float(input('Enter Base: '))
        print('Area of Square is : %0.1f' %(l*b))
    if i == 2:
        l = float(input('Enter Length: '))
        b = float(input('Enter Base: '))
        print('Area of Rectangle is : %0.1f' %(l*b))
    if i == 3:
        l = float(input('Enter Length: '))
        b = float(input('Enter Base: '))
        print('Area of Triangle is : %0.1f' %((l*b)/2))
    if i == 4:
        l = float(input('Enter radius: '))
        print('Area of Circle is : %0.1f' %(math.pi*l*l))
    
area(s)


