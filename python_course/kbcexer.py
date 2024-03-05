questions = [
    ["Which mobile brands popular in the wrold",
    "Xiomi","iphone", "Samsung" ,"HTC",4],
    
    ["Which mobile brands popular in the wrold",
    "Xiomi","iphone", "Samsung" ,"HTC",4],

    ["Which mobile brands popular in the wrold",
    "Xiomi","iphone", "Samsung" ,"HTC",4],

    ["Which mobile brands popular in the wrold",
    "Xiomi","iphone", "Samsung" ,"HTC",4],

    ["Which mobile brands popular in the wrold",
    "Xiomi","iphone", "Samsung" ,"HTC",4],
    
    ["Which mobile brands popular in the wrold",
    "Xiomi","iphone", "Samsung" ,"HTC",4],
]
levels = [10_000,30_000,50_000,70_000,100_000,120_000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a.{question[1]}            b.{question[2]}")
    print(f"d.{question[3]}            d.{question[4]}")
    reply = int(input("enter the answer (1-4) : "))
    if(reply == question[-1]):
        print(f"Correct Answer is, you have won rs {levels[i]}")
        if(i == 4):
            money = 10_000
        elif(i == 9):
            money = 20_000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer")
        break