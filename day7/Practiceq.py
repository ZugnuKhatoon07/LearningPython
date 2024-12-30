# #_______****Creat a nem file "practice.txt" using python. add the following data in it:****__________
# #hi everyone
# #we are learning File i/o
# #using Java.
# # I like prognamming in Java

f = open("Z:\\python\\day7\\practice.txt","w")
f.write("hi everyone\nwe are learning File i/o\nusing Java.\nI like prognamming in Java")

# #__________***WAP that replaces all occurrences of "Java" with "python" in above file.***_________
with open("Z:\\python\\day7\\practice.txt","r") as f:
    data = f.read()

new_data = data.replace("java","Python")
print(new_data)

with open("Z:\\python\\day7\\practice.txt","w") as f:
    data = f.write(new_data)


# f.write("hi everyone\nwe are learning File i/o\nusing python.\nI like prognamming in python")


# ________****Search if the word "learning" exists in the file or not.***____________
# word = "learning"
# with open("Z:\python\day7\practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")


def check_for_word():
    word = "learning"
    with open("Z:\python\day7\practice.txt","r") as f:
        data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")
    
def check_for_word():
    word = "learning"
    data = True
    line_no = 1
    with open("Z:\python\day7\practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

        return -1
print(check_for_word())

#____________****Frome a file containing separated by comma, print the count of even number.***_________
count = 0
with open("Z:\python\day7\practice.txt", "r") as f:
    data = f.read()
    # print(data)
    # print(type(data))

# num = ""
# for i in range(len(data)):
#     if(data[i] == ","):
#         print(int(num))
#         num = ""
#     else:
#         num += data[i]

nums = data.split(",")
for val in nums:
    if(int(val) % 2 == 0):
        count += 1

print(count)
