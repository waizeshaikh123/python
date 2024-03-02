#  @@@@@@ create calculater
first = input("Enter A number : ")
selectDigit = input("+,-,*,/:")
secound = input("Enter Secound NUmber :")
first = int(first)
secound = int(secound)

if(selectDigit == "+"):
    print(first + secound)
elif(selectDigit == "-"):
    print(first - secound)
elif(selectDigit == "*"):
    print(first * secound)
elif(selectDigit == "/"):
    print(first / secound)
else:
    print("Invalid Number")