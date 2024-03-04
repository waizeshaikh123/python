tab = (input("Enter the number : "))
print(f"Multipplication table of {tab} is ")

def func():
    
    try:
        for i in range(1,11):
            print(f"{int(tab)} X {i} = {int(tab)*i}")
    except:
        print("Please type num the number")
        return 2

    finally:
        print("always be execute")    
func()    
# table = input("Enter the number : ")

# try:
#     for i in range(1,11):
#         print(f"{int(table)} X {i} = {int(table)*i}")
# except:
#     print("Invalid synttex")