#1
str1="this is a string. \nwe are creating in python"
print(str1)
str2="hello I am Ayushi.\texcited"
print(str2)

#2
str1="Ayushi"
str2="Sahani"
print (str1+str2)
print(len(str1))
print(str1[1])
print (str1 [1:len(str1)])
print(str1[:4]) #[0:4]
print(str1[5:]) #[5:len(str1)]

# backward index
#1
str="Ayushi"
print(str[-5:-1])

#2
str="i love IIT Bombay"
print(str.endswith("bay")) #true
print(str.endswith("bom")) #false
str=str.capitalize() #captalise the first character and make other all lowercase
print(str)

print (str.replace("i","o"))
print (str)
print(str.find("o")) 
print(str.find("love"))
print(str.count("i"))

#3
age=12
if(age>=18):
    print("can vote")
    print("can drive")

#4
light="green"
if(light=="red"):
    print("stop")
elif(light=="green"): #else if   
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken") #indentation 4 spaces

# Nesting
#1
age=int(input("age"))
if(age>=18):
    if(age>=80):
        print ("cannot drive")
else:
    print ("can drive")


#2
a=int(input("a"))
if (a%2==0):
   print("even")  
else:
   print("odd")


#2
a=int(input("a"))
b=int(input('b'))
c=int(input("c"))

if (a>b and a>c):
    print(a)
elif(b>c):
    print(b)   
else:
    print(c)
    
#3
num=int(input("given number:"))
if(num%7==0):
    print("multiple of 7")
else:
    print("not a multiple")
