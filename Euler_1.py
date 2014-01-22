#-------------------------------------------------------------------------------
# Name:        Euler_1
# Purpose:     Provides a solution to problem 1 on Project Euler which is as
#              follows:
#              _________________________________________________________________
#              If we list all the natural numbers below 10 that are multiples
#              of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#              Find the sum of all the multiples of 3 or 5 below 1000.
#              _________________________________________________________________
#
# Author:      Robert J. Cassidy
#
# Created:     22/01/2014
# Copyright:   (c) Robert J. Cassidy 2014
# Licence:     GNU-GPL
#-------------------------------------------------------------------------------

def main():

    # Will store all verified values
    multiples_of_3_or_5 = []

    # Initializes the variable that will hold the sum of all values
    # Contained within list variable "multiples_of_3_or_5"
    multiple_summed = 0

    # Specifies the upper/lower bounds of values to check. The problem specifies
    # natural numbers below 1000 and therefore this variable has been set
    # accordingly,but could easily be set to any other values if necessary
    check_lower_bound = 0
    check_upper_bound = 1000

    # The following function will check to see if the input value is a
    # multiple of 3 or 5 and return True if either condition is satisfied
    # or False if neither conditions are met
    def is_multiple_of_three_or_five(number):
        if number%3==0 or number%5==0:
            return True
        else:
            return False

    # The following loop will call the function is_multiple_of_three_or_five
    # on numbers i in the range between check_lower_bound and
    # check_upper_bound1+1 (plus 1 so that the bound is included in the range),
    # and add them to multiple_summed if is_multiple_of_three_or_five
    # returns true
    for i in range(check_lower_bound, check_upper_bound):
        if is_multiple_of_three_or_five(i)==True:
            multiple_summed += i

    # Prints final answer stored in multiple_summed upon loop completion
    print "The sum of all multiples of 3 or 5 between "+ str(check_lower_bound)\
    +" and "+ str(check_upper_bound)+" is "+str(multiple_summed)+" !"

if __name__ == '__main__':
    main()
