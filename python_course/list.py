name = [1,2,3,4,6,7,9,0,6,4,7]
# # number = [2,3,5,6,89,5,6,7,8,0] 
# name.append("arish")
# name.sort()
# name.reverse()
# name.index("waize")
# print(name.count(4))
# l = (name.copy())
# l[9] = 3
# print(l)
# # print(type(name))
# # print(name[1:6:3])
# name.insert(1, 3)
m = [99,999,88]
m.extend(name)
print(m)
# ini = input(name)
# if ini in name:
#     print("Yes")
# else:
#     print("No")

# num = [2,4,5,87,6,3,9,43,10,44,22]

# for i in num:
#     if i%2==0:
#         print(i)
        
table = int(input("Enter the number: "))

for i in range(1,11):
    print(table,"X", i ,"=",table*i)

#  ############## list comprehensive
# li = [i for i in range(11) if i%2==0]
# print(li)