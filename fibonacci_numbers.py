# Fibonacci numbers   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Implment a program that will print a LIST of fibonacci numbers to a specified length.

# Example: fibonacci(10)
# input: number  (desired length of array)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] - the first 10 numbers of the fibonacci sequence

# Hint:
# You may start your array like this:
# list = [0, 1]


# *** your code here ***
# def fibonacci(num):
#     fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
#     print(fibonacci_numbers[:num])
# fibonacci(30)



def Fibonacci2(n):
    number = [0, 1, 1]
    for i in range(n):
        number.extend([number[i + 1] + number[i + 2]])
    return number
# Driver Program
 
print(Fibonacci2(1))