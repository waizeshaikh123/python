import random

def check(compter, user):
    if (compter == user):
        return 0
    if (compter == 0 and user == 1):
        return -1
    if (compter == 1 and user == 2):
        return -1
    if (compter == 2 and user == 0):
        return -1
    return 1


compter = random.randint(0,2)
user = int(input("0 for snkae , 1 for water and 2 for Gun\n"))

print("user is",user)
print("computer is",compter)

score = check(compter,user)
if(score == 0):
    print("Its a draw")
elif(score == -1):
    print("You won")
else:
    print("You lose")