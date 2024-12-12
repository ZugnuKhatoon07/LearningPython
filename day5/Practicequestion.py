#_________****Print number from 1 to 100.***_________
count = 1
while count <= 100 :
    print(count)
    count +=1
print("loop end")

#________****Print numbers from 100 to 1.***_______
i = 100
while i >= 1 :
    print(i)
    i -= 1
print("loop end")


#_________****Print the multiplication table of a number n.****_______
n = int(input("enter any number:"))
i = 1
while i <= 10 :
    print(n*i)
    i += 1


#____________****Print the elements of the following list using a loop :
# [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
heroes = ["ironman","thor","superman","batman"]
#traverse
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1
# idx = 0
# while idx < len(nums) :
#     print(nums[idx])
#     idx += 1


#_______***Search for a number x in this tuple using loop:***_______
#(1,4,9, 16,25,45,36,100)

nums = (1,4,9, 16,25,45,36,100,25)
x = 25
i = 0 #initialization
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
    else :
        print("finding..")
    i += 1

#_____________****(Break & continue) break : used to terminate the loop when encountered.****_________
i = 1
while i <= 5 :
    print(i)
    if(i==3):
        break
    i += 1 
    
#______****Continue : terminates execution in the curren iteration & continues execution of the loop with the net iteration.***_________
i = 0 
while i < 5 :
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

# _____***skip even***_________
i = 0 
while i < 10 :
    if(i %2 == 0):
        i += 1
        continue
    print(i)
    i += 1

# ____________**** skip odd nomber *******________
i = 0
while i < 10 :
    if(i %2 != 0):
        i += 1
        continue
    print(i)
    i += 1

#____________****for practiceuestion***_____________
#print the element of the following list using a loop :
nums = (1,4,9,16,25,36,49,64,81,100)
x = 49

idx = 0
for val in nums :
    if(val == x):
        print("number found at idx",)
    idx += 1


#range(start?,stop,step?)
for el in range(5):
    print(el)
for el in range(1,5):
    print(el)
for el in range(1,5,2):
    print(el)


#____________*****Forloop Practicequestion****____________
#print numbers from 1 to 100.
for i in range(1 , 101):
    print(i)


#___________****print numbers from 100 to 1.***_________
for i in range(100,0,-1):
    print(i)

#__________***print the multiplication table of a number n.***___________
n = int(input("enter any number :"))
for i in range(1, 11):
    print(n*i)

#________***Pass Ststement***_________
# pass is null ststement thst does nothing . it is used as a placeholder for future code.
for i in range(5):
    pass

if i > 5:
    pass

print("some usefil work")

#___________***WAP to find the sum of first n numbers . (using while)****________
n = int(input("enter any number :"))
sum = 0
for i in range(1, n+1):

    sum += i
    i += 1
print("total sum =",sum)

#WAP to find the factorial of first n numbers 
n = 5 
fact = 1
i = 1
while i <= n :
    fact *= i
    i += 1
print("factorial=", fact)
