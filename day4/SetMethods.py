# ________****adds an element****__________
collection = set ()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(3)
# #collection.remove(1)
collection.add("zugnujaan")
#collection.add({5}) #dict ko nahi likh sakte hai. 
#collection.add([4]) #list ko nahi likh sakte hai.
#collection.clear()


print(len(collection))
print(type(collection))

#______________*****removes the elem an ****_____________
number = {2,3,3,4,5,6}
number.remove(3)
print(number)

#__________****clear the elem an ****______________
number = {2,3,3,4,5,6}
number.clear()
print(number)

#________****removes a rondom value***___________
number = {2,3,3,4,5,6}
number.pop()
print(number)

#_____________****combines both set values & returns new***__________
set1 = {1,2,3,}
set2 = {3,4,5}
print(set.union(set2))
print(set1)
print(set2)

#__________****combines common values & returns new****_________
set1 = {1,2,3,}
set2 = {3,4,5}
print(set1.intersection(set2))





