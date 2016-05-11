# Name:
# Section:
# homework_2.py

##### Template for Homework 2, exercises 3.1-3.4  ######


# **********  Exercise 3.1 **********

# Define your rock paper scissors function here
##### YOUR CODE HERE #####

player_one = raw_input("Player 1 name?: ")
print "Welcome, ", player_one
print""

player_two = raw_input("Player 2 name?: ")
print "Welcome, ", player_two
print""

def rps(user1, user2):
  one = user1
  two = user2
  if one == "rock" and\
    two == "rock":
    print "Tied!"
  elif one == "paper" and\
    two == "paper":
    print "Tied!"
  elif one == "scissors" and\
    two == "scissors":
    print "Tied!"
  elif one == "rock" and\
    two == "scissors":
    print player_one, "wins!"
  elif one == "scissors" and\
    two == "paper":
    print player_one, "wins!"
  elif one == "paper" and\
    two == "rock":
    print player_one, "wins!"
  elif two == "rock" and\
    one == "scissors":
    print player_two, "wins!"
  elif two == "scissors" and\
    one == "paper":
    print player_two, "wins!"
  elif two == "paper" and\
    one == "rock":
    print player_two, "wins!"
  else:
    print "Those aren't valid options"

# Test Cases for Exercise 3.1
##### YOUR CODE HERE #####

rps("rock", "paper") #Player two wins
rps("scissors", "paper") #Player one wins
rps("car", "rock") #Those aren't valid options!
print""
# *********** Exercise 3.2 ***********
import math
import random
## 1 - multadd function
def multadd(a,b,c):
  return a * b + c

print"1+2 * 3"
print multadd(1,2,3) # =>5
print"\n2+2 * 2"
print multadd(2,2,2) # =>6
print"\n5+10 * 15"
print multadd(5,10,15) # => 65
print ""

## 2 - Equations

#Math Functions we need
sin = math.sin
cos = math.cos
pi = math.pi

angle_test = multadd(cos(pi/4),1.0/2,sin(pi/4))
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = multadd(math.log(144),1.0/math.log(7),math.ceil(276.0/19))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
def yikes(n):
  a = (math.e**x-1)**0.5
  b = math.e**(-x/2.0)
  c = x*math.e**(-x)
  print multadd(a,b,c)

# Test Cases
x = 5
print "yikes(5) =", yikes(x)

# ********** Exercise 3.3 **********

## 1 - rand_divis_3 function
def rand_divis_3():
  num = random.randint(0,10000)
  print "Randomly chosen from 0 - 10000: ", num
  if num%3 ==0:
    print "Divisible by three!"
  else:
    print "Not divisible by three :-("


# Test Cases
rand_divis_3()
rand_divis_3()
rand_divis_3()

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has

def roll_dice(a,b):
  count = b
  print "\nRolling a %d sided dice, %d times" % (a, b)
  while count > 0:
    print random.randint(1, a)
    count = count - 1


# Test Cases
roll_dice(6,3)
roll_dice(20,5)

