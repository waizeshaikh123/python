# ep = {33:4, 44:55, 77:88}
# ep2 ={73:33,55:66} 
# ep.update(ep2)
# print(ep)

dic = {
    1: 31, 2: 23,  3: 234
}
# p = dic.pop()
# p = dic.clear()
# p = dic.popitem()
p = dic.popitem()
del p[3]
print(p)
# print(dic.keys())
# print(dic.values())

# for key,value in dic.items():
    # print(key,value)