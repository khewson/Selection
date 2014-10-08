#Kim Hewson
#08/10/14
#Selection Spotcheck

attendance=int(input("Enter your attendance as a percentage: "))
if attendance>=85:
    print ("Your attendance is {0}%. Keep up the good attendance".format(attendance))
elif attendance<85:
    print ("Your attendance is only {0}%. You must improve your attendance to stay on the course".format(attendance))
