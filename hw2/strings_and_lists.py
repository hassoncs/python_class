# Name:
# Section:
# strings_and_lists.py

# **********  Exercise 4.1 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])

#Cumulative sum: Create a new list where each item is the sum
# of the previous numbers plus current
def cumulative_sum(number_list):
    sum = []
    total = 0
    for x in number_list:
        total += x
        sum.append(total)

    print sum

#Test Cases
print "\ncumulative_sum([1,2,3])"
cumulative_sum([1,2,3])
print "\ncumulative_sum([4,3,6])"
cumulative_sum([4,3,6])
print "\ncumulative_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])"
cumulative_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])


# **********  Exercise 4.2 **********

# Write any helper functions you need here.
# Below function accounts for both HW2 pig-latin and the optional pig-latin add-ons

VOWELS = ['a', 'e', 'i', 'o', 'u']
import string

def pig_latin():
    n = raw_input("\nEnter a phrase. Go ahead. Use numbers & punctuation if you want.\nWatch what happens:\n").lower()
    exclude = set(string.punctuation) # Targeting punctuation
    n = "".join([i for i in n if not i.isdigit()]) #Stripping numbers away
    n = "".join(i for i in n if i not in exclude) #Stripping punctuation away
    words = n.split(" ")
    result = []
    for x in words:
        if x[0].lower() in VOWELS:
            word = (x + "hay")
            result.append(word)
        else:
            end_char = x[0].lower()
            word = (x[1:] + end_char + "ay")
            result.append(word)
    for j in result:
        print j

pig_latin()

# **********  EXTRA! Optional Part 2 *********

def find_instances(n):
    integers = False
    for x in n:
        if isinstance(x,int) == True:
            integers = integers + 1
    if integers > 0:
        print "\nWe have integers!"
    else:
        print "\nNo ints in this list."
    print "Integers: %d" % integers +""

find_instances(["Hello"])
find_instances([12345])
find_instances(["Hello", 12345, 4938, 23423, 0, "LOL"])

