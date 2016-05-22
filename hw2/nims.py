# Name:
# Section:
# nims.py

def play_nims(pile, max_stones):
  print"Let's play stones!\n Pile: %r stones\n Max Stones: %r" % (pile, max_stones)

#   '''
#   An interactive two-person game; also known as Stones.
#   @param pile: the number of stones in the pile to start
#   @param max_stones: the maximum number of stones you can take on one turn
#   '''
## Basic structure of program (feel free to alter as you please):
#    while [pile is not empty]:
#        while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
#
#        while [player 2's answer is not valid]:
#            [ask player 2]
#            [execute player 2's move]
#
#    print "Game over"

  valid1 = False
  valid2 = False
  while pile > 0:
    vaild1 = False
    while valid1 == False :
      one_turn = input("\nPlayer 1. How many stones will you take? (Choose between 1 and %d):\n" % max_stones)
      if (one_turn <= max_stones) & (one_turn >=1):
        pile = pile - one_turn
        valid1 = True
        valid2 = False
        print "There are %s stones remaining." % pile
      else:
        print "That's not a valid option!"

    valid2 = False
    while valid2 == False:
      two_turn = input("\nPlayer 2. How many stones will you take? (Choose between 1 and %d):\n" % max_stones)
      if (two_turn <= max_stones) & (two_turn >=1):
        pile = pile - two_turn
        valid2 = True
        valid1 = False
        print "There are %s stones remaining." % pile
      else:
        print "That's not a valid option!"

  print "Game over!"
play_nims(100, 10)