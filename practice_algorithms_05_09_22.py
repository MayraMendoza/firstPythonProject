#________________________________________ 1____________________________________
# create a function which returns the number of True values in a list.
# if list is empty return a 0
# https://edabit.com/challenge/wFpi2zFGxWxfj5mZS

def count_true(lst):
    num_true = 0
    for x in lst:
        if(x == True):
            num_true += 1



    return num_true

#________________________________________ 2 ____________________________________
#Difference of Max and Min Numbers in List
#https://edabit.com/challenge/XsJLwhAddzbxdQqr4
#Create a function that takes a list and returns the difference between the biggest and smallest numbers.
def difference_max_min(lst):
    max=-1000
    min =1000

    for x in lst:
        if(x>max):
            max = x
        if(x < min):
            min = x

    difference = max - min
    return difference


##______________________________________ 3____________________________________
#https://edabit.com/challenge/9zsDKijmBffmnk9AP
#You hired three programmers and you (hopefully) pay them.
# Create a function that takes three numbers (the hourly wages of each programmer)
# and returns the difference between the highest-paid programmer and the lowest-paid.

def programmers(one, two, three):
    max = -100000
    min = 100000

    employees = [ one, two, three]

    for x in employees:
        if x > max :
            max = x
        if x < min :
            min = x

    difference = max - min
    return difference

##### after completing looked through solutions to show me how to approch this with built in methods

def programmers(one, two, three):

    employees = [ one, two, three]
    difference = max(employees) - min(employees)
    return difference



#bonus
#https://edabit.com/challenge/vxKcxazrqgmNA64db
#A word has been split into a left part and a right part.
# Re-form the word by adding both halves together, changing the first character to an uppercase letter

def get_word(left, right):
	new_word = left + right
	return new_word.capitalize()



#________________________________________ 4 ____________________________________
#https://edabit.com/challenge/GWPQ7XcbFBeS72xmv
#scoring system
#Andy, Ben and Charlotte are playing a board game. The three of them decided to come up with a new scoring system.
# A player's first initial ("A", "B" or "C") denotes that player scoring a single point.
# Given a string of capital letters, return a list of the players' scores.
#For instance, if ABBACCCCAC is written when the game is over, then Andy scored 3 points, Ben scored 2 points, and
# Charlotte scored 5 points, since there are 3 instances of letter A, 2 instances of letter B, and 5 instances of letter C. So the list [3, 2, 5] should be returned.

def calculate_scores(txt):
    num_a = txt.count('A')
    num_b = txt.count('B')
    num_c = txt.count('C')

    scores = [ num_a, num_b, num_c]

    return scores



#________________________________________ 5____________________________________
#https://edabit.com/challenge/hgHMhpJjyFxYJMMXp
#Get the file name
#Create a function that returns the selected filename from a path including the file extension.


def get_filename(path):
    parse_string = path.split("/")
    file_name = parse_string[len(parse_string)-1]
    return file_name


