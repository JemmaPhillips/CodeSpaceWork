def calculate_factorial(n):
    # Check if the input is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Initialize the result to 1
    result = 1

    # Calculate factorial
    for i in range(1, n + 1):
        result *= i

    return result

# Test the function with an example
number = 6
factorial_result = calculate_factorial(number)
print(f"The factorial of {number} is: {factorial_result}")
