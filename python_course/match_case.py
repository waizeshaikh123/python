i = input("Enter the value of i : ")
match i:
    case 0:
        print(i, "is not 50");
    case 1:
        print(i, "is not 70");
    case _ if i  != 90:
        print(i, "is not 90");
    case _ if i != 70:
        print("invalid");