val = str(input("Enter the value is :"));

if(val == "quite" or val == "Quite"):
    print ("You said quite");
    print("you complate the task")
else:
    raise  ValueError(" is an invalid input")
