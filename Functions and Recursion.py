#Functions
# a=5
# b=10
# sum=a+b
# print (sum)

# def cal_sum(a, b):
#     sum=a+b
#     print (sum)
#     return sum

# cal_sum (5, 10)

# def cal_sum(a,b): #parameters
#     return a+b
# sum= cal_sum(2,3) #function call , arguments
# print (sum)

# def print_hello():
#     print("hello")
# output=print_hello()
# print(output) #NOne

# Funtion types
# Built in
# print("Ayushi", end="ayu") #sep=' '
# print("sahani") #end="/n"

# User Defined
# def cal_prod(b, a=2):
#     print(a*b)
#     return a*b

# cal_prod(1)

# cities=["mumbai", "delhi", 'pune']
# def print_list(list):
#     for item in list:
#         print (item, end=" ")

# print_list(cities)

# def cal_fact(n):
#     fact=1
#     for i in range (i, n+1):
#         fact +=i
#     print(fact)

# cal_fact(6)

# recursion
# def show(n):
#     if (n==0): #base case
#         return
#     print (n)
#     show(n-1)

# show(5)

def print_list (list, idx):
    if (idx== len(list)):
        return
    print (list[idx])
    print_list (list,idx+1)




