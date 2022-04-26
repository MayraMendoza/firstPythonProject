print("welcome")

#name = input("what is your name?")




careerdevs = ["gabe", "magie", "cliff", "Arnell"]
accept = input("do you work at careerdevs? \n(yes/no)\n")

if accept == "yes":
    name = input("what is your name? ")
    for emp_name in careerdevs:
        if (name == emp_name):
            print("welcome")
    else:
        print("you are not an employee")

else:
    print("okay, ypu can leave")