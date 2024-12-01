#________****returns all keys****___________
zugnu = {
    "zaguu" : "jaan",
    "fiv" : {
        "black" : "coluor"

    }
}
# print(zugnu["fiv"])
print(zugnu.keys())

# ______________****returns all values****__________
student = {
    "name" : "zugnu khatoon",
    "subjects" : {
        "English" : 97,
        "operating system" : 99,
        "maths" : 100,
        "sad" : 98,
        "C programming" : 90,

    }

}
 
print(list(student.values()))


# _____________****myDic.items() #returns all (key ,vall) pairs as tuples
student = {
    "name" : "zugnu khatoon",
    "subjects" : {
        "English" : 97,
        "operating system" : 99,
        "maths" : 100,
        "sad" : 98,
        "C programming" : 90,

    }

}

# print(list(student.items()))
pairs = list(student.items())
print(pairs[1])

#_______****myDict.get("key") #returns the key according to value
student = {
    "name" : "zugnu khatoon",
    "subjects" : {
        "English" : 97,
        "operating system" : 99,
        "maths" : 100,
        "sad" : 98,
        "C programming" : 90,

    }

}
print(student["name"]) 
print(student.get("name"))

print(student["name2"]) #error
print(student.get("name2")) #no error -> none