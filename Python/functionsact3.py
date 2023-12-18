def is_prime(number):
    # Check if the number is a non-negative integer
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")

    # 0 and 1 are not prime numbers
    if number < 2:
        return False

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Number is divisible by i, not prime

    return True  # Number is prime

# Test the function with an example
test_number = 17
if is_prime(test_number):
    print(f"{test_number} is a prime number.")
else:
    print(f"{test_number} is not a prime number.")
