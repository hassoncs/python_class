#Joel Shooster
#5.10.16
#Zellers.py

print "********** Exercise HW1 Optional - Zellers **********"

#The best way to test this program is by first using today's date as the input
#It should return the day of the week that is today.

def get_info():
  months = [11, 12,1,2,3,4,5,6,7,8,9,10]
  days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  valid = False
  while valid == False:
    try:
      first_name = raw_input("Enter your first name: ")
      last_name = raw_input("Enter your last name: ")
      month = input("What month were you born? (please choose between 1 and 12, no zeroes): ")
      day = input("Day? ")
      year = input("Year? (XXXX format) ")
      print month
      if(month >=1) & (month <= 12):
        valid = True
      else:
        print "That's not a valid selection"
    except (NameError, ValueError, TypeError, SyntaxError):
      print "That's not a valid integer"

  print "You are %s %s. You were born %s / %d / %d"  % (first_name, last_name, month, day, year)
  #
  month = months[month-1]
  year = str(year)
  century = int(year[:2])
  year = int(year[-2:])
  if (month == 11) | (month == 12):
    year = year - 1
  print "Month index: ", month
  print "Century: ", century
  print "Year: ", year

  # Now comes the fun math part. Yay!
  W = (13*month-1) / 5
  X = year / 4
  Y = century / 4
  Z = W + X + Y + day + year - (2*century)
  result = Z % 7

  print "\n%s %s was born on a %s" % (first_name, last_name, days[result])

print "We will return the day of the week in which you were born"
print "Sunday is 0, Monday is 1, Tuesday is 2, etc..."
get_info()

