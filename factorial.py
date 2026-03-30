def factorial(n):
    if n==0:
        return
    return n*factorial(n-1)
n=3
print(factorial(n))

#secomd method
def factorial2(X):
    ans = 1

    # Loop from 1 to X to compute factorial
    for i in range(1, X + 1):
        ans *= i

    # Return the final result
    return ans

# Input value for which factorial is to be calculated
X = 5

# Call the factorial function and store the result
result = factorial2(X)

# Print the result
print(f"The factorial of {X} is {result}")