students = ['Mayra', 'Melissa', 'Ella', 'Joe', 'Mike', 'Tim']
print ('Welcome!')
accept =input('Are you a student? \n(yes/no)')

student_name = input('what is you name ?\n')

for x in students:
    if(x == student_name):
        print('Welcome to class')
        break
    else :
        print('you do not belong here')

