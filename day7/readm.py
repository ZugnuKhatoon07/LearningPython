#___________****Read entire file***____________
f = open("Z:\python\day7\zugnu.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

# ***_____For the letter the needs to be read***_______
f = open("Z:\python\day7\zugnu.txt","r")
data = f.read(5)
print(data)
print(type(data))
f.close()

#________****read one line at a time****__________
f = open("Z:\python\day7\zugnu.txt","r")
# data = f.read()
# print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

print(type(data))
f.close()


