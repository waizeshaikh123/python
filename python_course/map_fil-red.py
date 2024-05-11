from functools import reduce
# Maping func()
# l = [1,4,6,3,4]
# newl = list(map( lambda x: x*x,l))
# print(newl)

# li = [1,2,3,4,5,6]
# newlll = list(map(lambda x: x*x , li))
# print(newlll)



# Filter  func()
# ll = [1,4,6,7,8,9]
# nl = list(filter(lambda x: x>3 ,ll))
# print(nl)


# li = [1,2,4,6,8,0,10,55]
# sum =set(filter(lambda x: x>3, li))
# print(sum)

# Reduce
# num = [1,2,3,4,5]
# newll = reduce(lambda x,y: x+y,num)
# print(newll)

li = [1,2,4,6,8]
sum =reduce(lambda x,y: x*y , li)
print(sum)