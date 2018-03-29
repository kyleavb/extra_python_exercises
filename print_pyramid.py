# Implement a program that prints out a half-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     #
    ##
   ###
  ####
 #####
######


# Challenge
# Implement a program that prints out a full-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     # #
    ## ##
   ### ###
  #### ####
 ##### #####
###### ######


# *** your code here ***
def pyramid(num):
    space = ' '
    pound = '#'
    for i in range(num):
        i += 1
        diff = num - i
        line = (diff * space) + (i * pound) + space + (i * pound) + (diff * space)
        print(line)

pyramid(10)
print(' ')
pyramid(5)
