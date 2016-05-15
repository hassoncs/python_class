#Joel Shooster
#5.10.2016
#Message Cipher

text = raw_input("Enter message. Don't be shy. \nUse whatever characters you want. We can translate it: ")
letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
punctuation = "!@#$%^&*()-[]}{|\/.,><~`;:'\"?"
#This is where we set the shift value. Right now it's set to 4.
c = 4
cipher = ""

# Now let's parse through the user's input. It can handle lowercase letters,
# uppercase letters, punctuation, and integers.
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
  elif x in punctuation:
    cipher += x
print("Your message: " + cipher)