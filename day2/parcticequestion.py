#_________***let's Practice***_________

#WAP to input user's first name & print its length.
name = input("enter any name : ")
# print(name)
# print(len(name))
print("length of your nsme is ", len(name))


#WAP to find the occurrence of '$'in a String.
str = "i am$ zugnu$ from siwan$","$99.99"
print(str.count("$"))

#conditional statements== grade students based on marks
# marks >= 90,grade = "A"
# 90  > marks >= 80, grade ="B"
# 80 > marks >= 70,grade ="c"
# 70 > marks,grade = "D"

marks = int(input("enter studedent marks : "))
if(marks >= 90):
    print("grade A")
elif(marks >=80 and marks < 90):
    print("grade B")
elif(marks >= 70 and marks < 80):
    print("grade C")
else:
    print("grade D")

#WAP to check if a number entered by the user is odd or eve.
num = int(input("enter any number :"))

if(num % 2 ==0):
    print("even")
else:
   print("odd")

#WAP to find the greatest of 3 numbers entered by the user.
a = 5
b = 7
c = 9
if(a > b and a > c):
    print("a")
elif(b > c):
    print("b")
else:
    print("c")

a = int(input("enter frist number : "))
b = int(input("enter frist number : "))
c = int(input("enter frist number : "))

if(a >= b and a >= c):
    print("frist number is largest",a)
elif(b >= c):
    print("second number is largest",b) 
else:
    print("thrid number is largest",c)   

#WAP to check if a number is a multiple of 7 or not.
x = int(input("enter any number :"))
if(x % 7 ==0 ):
    print("multiple of 7")
else:
    print("not a miltiple")


