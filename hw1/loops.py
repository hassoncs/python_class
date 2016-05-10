#Joel Shooster
#HW 1 - Loops
#Date: 5/9/2016
#Loops.py

print "Name: Joel Shooster"
print "Section: HW 1 - Loops"
print "Date: 5/9/2016"
print "loops.py"

print "A loop that prints decimal equivalents..."
for x in xrange(1,11):
  print "1/%d converted to decimal is: " % x, 1.0 / x


# I tried breaking this one every which way! It's our while-loop
print"\nNow a function that counts down from a user-selected, positive integer"
def get_num():
  valid = False
  while valid == False:
    try:
      num = input("Select a positive integer: ")
      if num > 1:
        countdown(num)
        valid = True
      elif num == 0:
        print "Zero? Really?"
      else:
        print "Negative number. Tsk tsk... "
    except NameError:
      print "That's not a valid integer"
    except ValueError:
      print "That's not a valid integer"
    except TypeError:
      print "That's not a valid integer"
    except SyntaxError:
      print "That's not a valid integer"

def countdown(n):
  while n > 0:
    print n
    n -= 1

#Now for that for_loop for exponentials
def get_exp_and_base():
  #This helps us cover our edge cases
  valid = False
  while valid == False:
    try:
      base = input("What is your base? : ")
      exp = input("What is your exponent? : ")
      if (base > 0) & (exp > 0):
        valid = True
      elif(base == 0) | (exp == 0):
        print "Zero? Really?"
      else:
        print "Negative number. Tsk tsk... "
    except NameError:
      print "That's not a valid integer"
    except ValueError:
      print "That's not a valid integer"
    except TypeError:
      print "That's not a valid integer"
    except SyntaxError:
      print "That's not a valid integer"

  #This is our FOR logic here!
  for x in xrange(1,base + 1):
    print x, " ** %d =" % exp, x ** exp

#Divide by two
def div_by_two():
  #This helps us cover our edge cases
  valid = False
  while valid == False:
    try:
      num = input("Give me something divisible by two: ")
      if num % 2 == 0:
        print "Yas! Divisible by two!"
        valid = True
      elif num == 0:
        print "Oh gosh... Not these zeroes again... "
      elif num % 2 != 0:
        print "Ummm.. NO!"
      else:
        print "Really? A negative number?"
    except NameError:
      print "That's not a valid integer"
    except ValueError:
      print "That's not a valid integer"
    except TypeError:
      print "That's not a valid integer"
    except SyntaxError:
      print "That's not a valid integer"

#Call our functions
get_num()
get_exp_and_base()
div_by_two()