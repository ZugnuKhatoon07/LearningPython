f = open("Z:\\python\\day7\\notes.txt", "r")
data = f.read()
print(data)
print(type(data))
# f.close()

f = open("Z:\\python\\day7\\notes.txt", "r")
data = f.read(40)
print(data)
print(type(data))

f = open("Z:\\python\\day7\\notes.txt", "r")
line1 = f.readline()
print(line1)
# print(type(data))

line2 = f.readline()
print(line2)

f.close()

