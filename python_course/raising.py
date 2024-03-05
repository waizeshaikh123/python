val = str(input("Enter the value is :"));

if(val == "quit" or val == "Quit"):
    print ("You quite");
    print("you complate the task")
else:
    raise  ValueError(" is an invalid input")
