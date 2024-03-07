from functools import reduce
# Maping func()
l = [1,4,6,3,4]
newl = list(map( lambda x: x*x,l))
print(newl)


# Filter  func()
ll = [1,4,6,7,8,9]
nl = list(filter(lambda x: x>3 ,ll))
print(nl)



# Reduce
num = [1,2,3,4,5]
newll = reduce(lambda x,y: x+y,num)
print(newll)
