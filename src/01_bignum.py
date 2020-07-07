# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)
import math
# YOUR CODE HERE
print (math.pow(2,65536)) 
# This will print out an OverflowError: math range due to it being way outside of the bounds of int max value
# In js it will print "Infinity"
