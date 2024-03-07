re = open('name.txt','r')
while True:
    line = re.readline()
    if not line:
        break
    print(line)