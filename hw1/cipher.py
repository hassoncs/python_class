#Joel Shooster
#5.10.2016
#Message Cipher

text = raw_input("Enter message: ")
letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
#This is where we set the shift value. Right now it's set to 4.
c = 4
cipher = ""

for x in text:
  if x in letters:
    cipher += letters[(letters.index(x)+c)%(len(letters))]
  elif x in upper_letters:
    cipher += upper_letters[(upper_letters.index(x)+c)%(len(upper_letters))]
  elif x in numbers:
    x = numbers[(numbers.index(x)+4)%(len(numbers))]
    x = int(x) % 6
    x = str(x)
    cipher += x
  elif x == " ":
    cipher += " "
print("Your message: " + cipher)