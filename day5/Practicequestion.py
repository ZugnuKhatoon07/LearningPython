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
    

