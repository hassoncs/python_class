#Joel Shooster
#5.10.2016
#Message Cipher

text = raw_input("Enter message: ")
letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = 3
cipher = ''

for x in text:
  if x in letters:
    cipher += letters[(letters.index(x)+c)%(len(letters))]
  elif x in upper_letters:
    cipher += upper_letters[(upper_letters.index(x)+c)%(len(upper_letters))]
  elif x == " ":
    cipher += " "

print("Your message: " + cipher)