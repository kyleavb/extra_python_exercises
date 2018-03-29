# Given an array of integers, every element appears twice except for one.
# Implement a program that will print that single one.

# Example: [1,1,2,2,3,3,4,5,5,6,6,7,7] - 4 would be the odd man out

# Note:
# Your algorithm should have a linear runtime complexity.


# *** your code here ***
def singleOut(data):
    single = []
    i = len(data)
    while 0 < len(data):
        if(data[i] == data[i - 1]):
            data.pop(data[i])
            data.pop(data[i-1])
        else:
            single.append(data[i])
            i += 1
    return single

test = singleOut([1,1,2,2,3,3,4,5,5,6,6,7,7])
print(test)
