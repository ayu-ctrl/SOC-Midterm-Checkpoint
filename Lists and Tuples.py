# list
# marks= [94, 87, 95, 66, 99]
# print (marks)
# print (type(marks))
# print(marks[0])
# print (len(marks))

# str= "Ayushi"
# print(str[0])
# str[0]= "B"     #not allowed

# student=["Ayushi", 100, 24, "Mumbai"]
# print(student[0])
# student[0]= "Anushka"
# print(student)
# print(student[2:4])   #same as slicing 

#list methods (same applied for string (not mutable) ) mutable
# marks=[2, 5, 1, 7]
# marks.append(6)
# print(marks)
# marks.sort() #ascending
# print(marks.sort())
# print(marks)
# print(marks.sort(reverse=True))
# print(marks)
# marks.reverse()
# print(marks)
# marks.insert(1, 4) 
# print(marks)
# marks.remove(3)
# print(marks)

# Tuples #same as lists but immutable
# tup=(2, 1, 4, 6)
# print(tup(0))
# # tup(0)=3 not allowed

# tup=(1,)   
# print(tup)

# tuple methods
# tup=(1, 2, 5, 2)
# print(tup.index(1)) #index of number 1
# print(tup.count(2)) 

 
list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else: 
    print("not a palindrome")
