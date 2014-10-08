#Kim Hewson
#08/10/14
#Selection Spotcheck

first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
gender=input("Enter your gender as a letter M/F: ")
if gender=="M":
    print("Mr {0} {1}".format(first_name,last_name))
elif gender=="F":
          print("Ms {0} {1}".format(first_name, last_name))
else:
    print("Please enter an appropriate gender")
