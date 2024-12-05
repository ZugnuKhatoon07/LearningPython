#______________*****Store following word meaning in a python dictionary :*****______________
#table : "a piece of furniture", "list of facts &figures"
# cat : "a small animal"

dictionary = {
    "cat" : "a small animal",
    "table" : ("a piece of furniture", "list of & figures")
}
print(dictionary)

#_____****you are giveb a list of subjects. Assume one classroom is reruired for 1 subject . how many classroom are needed by all student.***__________
# "python", "java", "c++", "python", "javascript","java","python","java","c++","c"
subject = {"python","java", "c++", "python", "javascript","java","python","java","c++","c"}
print(len(subject))

#_______****WAP to enter marks of 3 subje ts from the user and store them in a dictionary.Start woth an empty dictionary & add one . use subject name as key & mrk as value.****_____________

marks = {}

z = int(input("enter english : "))
marks.update({"english" : z})

z = int(input("enter math : "))
marks.update({"math" : z})

z = int(input("enter operating system : "))
marks.update({"operating system" : z})

z = int(input("enter sad : "))
marks.update({"sad" : z})

z = int(input("enter c programming : "))
marks.update({"c programmin" : z})

print(marks)

#______****figur out a way to 9 & 9.0 as separate values in the set . (you can take help of built-in data types)***_____________
values = {9 , 9.0, 9.25, 8, 8.0}
print(values)

values = {
    ("int", 9,),
    ("float",9.0)
}
print(values)





