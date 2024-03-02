# tup = (1,3,5,7,3,45,5,3,8,2)
# # print(type(tup),tup)
# # print(tup[0])
# # print(tup[-1])
# # print(tup[2])
# # print(tup[3])
# # print(tup[1:4])

# res = tup.index(3, 4, 5)
# print("Count of 3 is ",res)



a = ("vivo", "oppo", "redmi", "realme", "samsung")
for i in range(len(a)):
    print(a[i])

x = 0
while x < len(a):
    print(a[x])
    x = x+1

print(a.count("realme"))
print("index of number is",a.index("realme"))