#___________***ovewrites the entire file****____________
f = open("Z:\\python\\day7\\zugnu.txt","w")

f.write("I want to learn javaScript tomorrow")

f.close()

#_____________****add to the file***__________
f = open("Z:\\python\\day7\\zugnu.txt","a")

f.write("\nThen I'll move to Reactjs")

f.close()

#_________****file ko esegst methode***________
f = open("saple.txt", "w")
f.close()

#____________***read and write***___________
f = open("Z:\python\day7\zugnu.txt","r+")
f.write("abc")
print(f.read())
f.close()

f = open("Z:\python\day7\zugnu.txt","a+")
# f.write("abc")
print(f.read())
f.write("abc")
f.close()