# loops
# i=1
# while i<5: 
#     print("hello") #infinite loop
# i=1
# while i<=5:
#     print("hello")
#     i+=1
# i=5
# while i>=1:
#     print(i)
#     i-=1
 
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x=36
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print(i)
#         break
#     i+=1

# break and continue
# i=1  
# while i<=5:
#     print(i)
#     if (i==3):
#         break
#     i+=1

i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue  #skip
    print(i)
    i+=1



