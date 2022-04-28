COMPANY_NAME = "Tech Inc."

EMPLOYEES = ["Alice", "Bob", "Cameron", "Dan", "Ellen", "Frank", "Grace", "Harry"]

# Welcome message + employee names listed out
print("\nWelcome to the "+COMPANY_NAME+" employee check-in\n")
print("We at " + COMPANY_NAME + " are very proud of our employees: ")
for emp_name in EMPLOYEES:
    print("-- "+emp_name)
print("\n")

# user input section (buggy code)

accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ").lower().strip()
#accept = accept.lower().strip()

while(accept != "yes" ) and (accept!= "no")  and (accept != "n") and (accept != "y"):
    accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ").lower().strip()
    print(accept)

if accept[0].lower() == "y":
    name = input("What is your name?\nName: ").lower().strip()
    if not name:
        name = input("What is your name?\nName: ").lower().strip()

    #name = name.strip()
    for emp_name in EMPLOYEES:
        if name == emp_name.lower():
            print("Thank you " + emp_name + ", you are now checked in.")
            break
    if name != emp_name.lower():
          print("You're not an employee")
else:
    print("This service is not for you. Exiting program...")
    exit()