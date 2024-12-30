with open("Z:\python\day7\zugnu.txt","r") as f:
    data = f.read()
    print(data)

with open("Z:\python\day7\zugnu.txt","w") as f:
    f.write("new data")