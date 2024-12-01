#___________****WAP to ask the user to enter name of their 3 favorite movies & store them in a list.****___________
movies = []
movies.append(input("enter frist movie name : "))

movies.append(input("enter second movie name : "))

movies.append(input("enter third movie name : "))

print(movies)

#__________****Wap to check if a list contains a palindrome of elements. (Hint: use copy()method)****_________
list1 = [1, 2,  1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

# ___________****WAP to count the number of student with the "A" grade in the fpllowing tuple.****__________
tup = ("c", "D","A","A","B","A")
print(tup.count("A"))

#  __________****store the above values in a list & sort them from "A" to "D".****____________
list = ("c", "D","A","A","B","A")
print(list.sort())
