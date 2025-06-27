#dictionary in pairs ("key" : value) unordered, mutable, duplicate keys not allowed
# me={
#     "topic":("dic", "set"),   #tupple
#     "name": "Ayushi",
#     "height": "5",
#     "hobby": "Modelling",
#     "age" : 19,
#     24:10,
#     "marks": [12, 24, 48]  #list
# }
# print(me)
# print(me["name"])
# me["name"]= "Anushka" #overwrite
# print(me)

# null_dict={}
# null_dict["name"]="aditi"

#nested dictionary
# student={
#     "name":"Ayush",
#     "sub":{
#         "phy":97,
#         "chem":98,
#         "maths":99
#     }
# }
# print(student["sub"]["maths"])
# print(student.keys())
# print(list(student.keys()))
# print(student.items())
# # print(student["name1"])    #error
# print(student.get("name1"))   #no error but none
# student.update({"city": "Delhi"})

#Set  mutable/ lekin uske elements immutable hote hai / lists aur dictionary ko isliyr paas nhi kar sakte
# set1={1,2,3,4,2,"hello"} #unordered and repeted elements are not allowed
# print(set1)

# collection={}  empty dictionary
# collection=set()  # empty set
# collection.add(1)
# collection.add(3)
# collection.remove(3)
# collection.add("Ayushi")
# collection.add("Ayushi")
# collection.add((1,2,3))
# # collection.add([1,2,3]) error lists
# print(collection)
# # collection.clear()
# print(collection.pop()) #pop random value
# print(collection.pop())

#union n intersection

# set1={1,2,3,4}
# set2={2,3,4,5}
# print(set1.union(set2))
# print(set1.intersection(set2))

# Questons
# a=int(input("a"))
# b=int(input("b"))
# c=int(input("c"))

# marks={}
# marks["mark1"]=a
# marks["marks2"]=b
# marks["mark3"]=c
# print(marks)

set1={9,9.0} 
print(set1)

set2={
    ("float", 9.0),
    ("int",9)
}
print(set2)

