print "Name: Joel Shooster"
print "Section: HW 1"
print "Date: 5/9/2016"
print "homework_1.py"
print ""
##### Template for Homework 1, exercises 1.2-1.4 ######

print "********** Exercise 1.2 **********"

print "Made the board into a variable so we can reuse it"

board = """
          |  |
        --------
          |  |
        --------
          |  |
"""
print board

print "********** Exercise 1.3 **********"
print"""If we want to make the board more than just a string, we ought to use
format strings to put some life into it. I turned the boxes into indeces on a tuple.
Below we have an empty board. However, this time it has 9 boxes ready to by used in a game.
"""

boxes = ["-","-","-","-","-","-","-","-","-"]
board = """
         %s | %s | %s
        ------------
         %s | %s | %s
        ------------
         %s | %s | %s
"""

print board % tuple(boxes)


print "For fun, let's change those box variables and see what happens when we run board again."
boxes = ["x", "o" , "o", "-", "x", "o", "-", "-", "x"]
boxes[3] = "o"
boxes[6] = "o"
boxes[7] = "x"

print board % tuple(boxes)
print "Not so empty anymore, huh?"
print "Now let's demonstrate how we could get user input...."

print "********** Exercise 1.4 **********"

first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")
dob = raw_input("Enter your date of birth: ")
month = raw_input("Month? ")
day = input("Day? ")
year = input("Year? ")

print"""
You are %s %s. You date of birth is %s.
The month is %s. Day is %d. Year is %d.
""" % (first_name, last_name, dob, month, day, year)


print "********** EXTRA **********"
print "... I got a bit carried away and wanted to manipulate tic-tac-toe more"
print ""
#This is how we make use of what we have above
print"Welcome to Tic-Tac-Toe!"
print""
boxes = ["-","-","-","-","-","-","-","-","-"]
possible_choices = [1,2,3,4,5,6,7,8,9]

print "We use raw_input for the player names as they are strings"
print ""
player1 = raw_input("Player1 name: ")
print "Hello, " + player1
print""
player2 = raw_input("Player2 name: ")
print "Hello, " + player2
print""

print "We use 'input' for choice as these are integers"
# def player1_turn
def player1_turn():
  valid = False
  while valid == False:
    try:
      choice = input(player1 + ", choose between 1 and 9 (and not one that has already been picked)")
      if choice not in possible_choices:
        print "That isn't a valid option"
      else:
        boxes[choice - 1] = "x"
        print "You chose ", choice
        print board % tuple(boxes)
        possible_choices.remove(choice)
        print possible_choices
        valid = True
    except NameError:
      print "That's not a valid integer"
    except ValueError:
      print "That's not a valid integer"
    except TypeError:
      print "That's not a valid integer"

def player2_turn():
    valid = False
    while valid == False:
      try:
        choice = input(player2 + ", choose between 1 and 9 (and not one that has already been picked)")
        if choice not in possible_choices:
          print "That isn't a valid option"
        else:
          boxes[choice - 1] = "o"
          print "You chose ", choice
          print board % tuple(boxes)
          possible_choices.remove(choice)
          print possible_choices
          valid = True
      except NameError:
        print "That's not a valid option"
      except ValueError:
        print "That's not a valid option"
      except TypeError:
        print "That's not a valid option"
      except SyntaxError:
        print "That's not a valid option"

player1_turn()
player2_turn()