"""
Moring time -> 12:00AM to 11:59AM
Afternoon time -> 12:00PM to 17:59PM
Evening time -> 18:00AM to 19:59AM
Night time -> 20:00AM to 23:59AM

"""
import time
name = input("Enter your name: ")
timee = int(time.strftime('%H'))
if timee <12:
    print("Good morning,",name)
elif timee >12 and timee < 18:
    print("Good Afternoon,",name)

elif timee >18 and timee < 20:
    print("Good Afternoon,",name)
else:
    print("Good night,",name)
