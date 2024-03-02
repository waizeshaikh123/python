
i = 60
while (i >= 1):
    print(i)
    i = i - 1
    if(i == 10):
        break


### braek 
for i in range(12):
        print("5 X ", i , "=" , 5 * (i))
        if (i == 8):
            break
# #  contineu
table = int(input('eter the value for table : '));
for i in range(12):
        print(table,"X", i , "=" , 5 * i)
        if (i == 8):
            print("skip for table line is", i )
            break;