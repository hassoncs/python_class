# Name:
# Section:
# homework_3.py

##### Template for Homework 3, exercises 5.1 - 5.5 ######

# **********  Exercise 5.1 ********** 

# Bugs
##### BUG 1 #####


##### BUG 2 #####


##### BUG 3 #####



# **********  Exercise 5.2 ********** 

# Define "Mutable" and list what data structures have this characteristic



# Define "Immutable" and list what data structures have this characteristic




# **********  Exercise 5.3 **********

def ball_collide(ball1, ball2):
    '''
    Computes whether or not two balls are colliding
    
    ball1: a tuple of (x-coord, y-coord, radius) nums (ints or floats);
        represents first ball
    ball2: a tuple of (x-coord, y-coord, radius) nums (ints or floats); 
        represents second ball

    returns: True if the balls collide and False if they do not collide
    '''
    ##### YOUR CODE HERE #####

    

# Test Cases for Exercise 5.3
# print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
# print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
# print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True


# **********  Exercise 5.4 **********

def add_class(class_num, desc, class_dict):
    '''
    Adds a class number/class name pair to a dictionary
    
    class_num: a string; the MIT number associated with the class
    desc: a string; the English name of the class
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; only modifies class_dict
    '''
    ##### YOUR CODE HERE #####
    
    

def print_classes(course, class_dict):
    '''
    Prints out all the classes you've taken in a given Course.
     If no classes were taken in the Course, print out that none were taken
    
    course: a string; the Course for which we would like to
     print out classes taken
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; simply prints out relevant information
    '''
    ##### YOUR CODE HERE #####

    

# Test Cases for Exercise 5.4
##### YOUR CODE HERE #####



# **********  Exercise 5.5 **********

def buildAddrBook(fileName):
    '''
    Builds an address book from a file.
    
    fileName: a string, the name of the file to read in
     File must be in the format specified in Exercise 5.5.

    returns: a dictionary with keys and values generated
      from the file, as specified in Exercise 5.5.
    '''
    ## Your Code Here ##
    


def changeEntry(addrBook, entry, field, newValue):
    '''
    Changes one entry in the specified address book.

    addrBook: a dictionary in the address book format
      returned by buildAddrBook.
    entry: a string; the pre-existing entry to change
    field: a string; the field to change (one of: "name",
      "phoneNumber", "emailAddress")
    newValue: the new value for the specified field

    returns: nothing; only modifies addrBook
    '''
    ## Your Code Here ##
