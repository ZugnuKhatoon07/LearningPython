#__________________****Conditional Statemrnts****____________
# 1
age = 21

if(age >= 18):
    print("can vote")
    print("csn drive")


#2
light = "green"

if(light == "red") :
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

print("end of code")

#3
num = 5
if(num > 2):
    print("greater than 2")
elif(num > 3):
    print("greter than 3")

#4
age = 24 
 
if(age >= 18):
    print("can vote")
else:
    print("can not vote")#....is space ko indentation kahte hai 

#nesting
if(age >= 18):
    if(age >= 80):
        print("can not drive")
    else:
        print("can drive")
else:
    print("cannot drive")

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



