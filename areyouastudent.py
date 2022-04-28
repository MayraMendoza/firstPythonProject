
def is_student(student_name, array):
    for name in array:
        if(name.strip().lower() == student_name.lower()):
            return 'y'

    else:
        return 'n'


students = ['Mayra', 'Melissa', 'Ella', 'Joe', 'Mike', 'Tim']


print ('Welcome!')
accept =input('Are you a student? \n(yes/no): ').lower().strip()

while  (accept != "n") and (accept != "y") and (accept != "yes" ) and (accept!= "no") :
    accept = input('Are you a student? \n(yes/no): ').lower().strip()

if(accept[0] == 'y'):
    student_name = input('what is you name ?\n').strip().lower()
    student_confirmation = is_student(student_name, students)
    if(student_confirmation == 'y'):
        print('welcome to class')
    else:
        print('you do not belong here, Have a nice day :) ')



####################################################################

# students = ['Mayra', 'Melissa', 'Ella', 'Joe', 'Mike', 'Tim']
# print ('Welcome!')
# accept =input('Are you a student? \n(yes/no): ').lower().strip()
#
# while accept[0].lower() != 'n' and accept[0].lower() != 'y'  :
#     accept = input('Are you a student? \n(yes/no): ').lower().strip()
#
# if(accept[0] == 'y'):
#     student_name = input('what is you name ?\n').strip().lower()
#     print(student_name)
#     for x in students:
#         if(x.strip().lower() == student_name):
#             print('Welcome to class')
#             break
#
#
#     else:
#         print('you do not belong here 1')
#
# else:
#     print('you do not belong here')