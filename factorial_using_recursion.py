
def find_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*(find_factorial(n-1))

print("Factorial of 5: ", find_factorial(5))