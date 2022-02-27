# from traceback import print_tb


# str1 = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'

# a=22
# b=27
# c=97
# d=102

# e=str1[0:6]
# f=str1[6:12]
# print(e+ ' ' + f)

# # Conditions and Loops
# a=42
# if a < 10:
#     print("The number is less than 10")
# else:
#     print("The number is greater than or equal to 10")

# greetings = 1
# while greetings <=3:
#     print('hello!' * greetings)
#     greetings = greetings + 1 

# # if you want to repeat an action exactly times, you can use the following template
# names = ['Alice', 'Bob', 'Charley']
# for name in names:
#     print ('Hello, ' + name)



# want to repeat an action exactly times, you can use the following template:
n = 10
for i in range(n):
    print (i)

a=100
b=200

for i in range(a, b):
    list1=[]
    if i % 2 == 1:
        list1.append(i)
    for n in range(list1):
        list1 += list1[n]