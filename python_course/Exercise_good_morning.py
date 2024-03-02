import datetime
import sys
# timesrtamp = int(time.strftime('%H, %M,  %S'))
# print(timesrtamp)

# wake = input("Enterf a wake-up section")
# if(wake == "morning"):
#     print("Wkae up morning");
# elif(wake  == "evening"):
#     print("Wake up evening");
# elif(wake == "afternoon"):
#     print("It's Afternoon! Take")
# else:
#     print("Invalid Input")



# #############1 version py
# print("Python version")
# print(sys.version)
# print(sys.version_info)


# #############2 Twinkle poem
twinkle = "Twinkle, Twinkle, little star,\n\thow are wonder what you are!\n\t\tup above the world so high\n\t\tLike a diamond in the sky\nTwinkle,Twinkle, little star,\n\tHow I wonder wat you are"
print(twinkle)



# #############3 current date time 
now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))