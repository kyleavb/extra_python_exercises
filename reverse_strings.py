# Reverse Strings in a Sentence

# Given a string, implement a program that will reverse the order of the characters
# in each word within a sentence while still preserving whitespaces and initial word order.

# Example:
# Input: "Let's do a coding challenge"
# Output: "s'teL od a gniedoc egnellahc"


# *** your code here ***
def string_reverse(string):
    return_str = string[::-1]
    return return_str
print('test string:  kyle cool')
print('expect: looc elyk')
print(string_reverse('kyle cool'))
