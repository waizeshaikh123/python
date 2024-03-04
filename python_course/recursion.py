def fact(f):
    if(f == 0 or f == 1):
        return 1
    else:
        return f * fact(f-1)
print(fact(3))
print(fact(8))
print(fact(10))
