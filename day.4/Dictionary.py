dict = {
    "key" : "value",
    "name" : "apnizaguu",
    "learning" : "cading",
    "zaguu" : "zaguu",
    "age" : 19,
    12.23 :35.56,
    "is_adult" : True,
    }
dict["key"] = "zagujaan" #overwrite
print(type(dict))
print(dict)
dict["zagujaan"] = "saruu"
print(dict)

#_______****Nested dictionary***___________
student = {
    "name"   : "zugnu katoon",
    "sunbject" : {
        "english" : 56,
        "chem" : 78,
        "phy" : 98,
        "math" : 90,
        "hindi" : 100,
    }
}
#print(student["subject"])
print(student.keys())

