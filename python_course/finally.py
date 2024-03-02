# def func1():
#     try:
#         l = [1,5,6,7]
#         i = int(input("Enter The index: "))
#         print(l[i])
#         return 1
#     except:
#         print("Some error occured")
#         return 0

#     finally:
#         print("I am always be executes")
        
# x = func1()
# print(x)

#  ######## raise error

# a = int(input("enter any number: "))
# if(a<5 or a>9):
#     raise ValueError("Value is not defined")

a =input("Enter a number:")
if(a == "quit"):
    raise ValueError("soory not defined")  
elif(a == 2):
    print("nothing")