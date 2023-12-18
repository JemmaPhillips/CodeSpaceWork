# generate Fibonacci series up to limit
def fibonacci_series(limit):
    fibonacci_sequence = [0, 1]  # sequence with the first two numbers

    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_number > limit:
            break
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# set limit to 50
limit = 50

# Get the Fibonacci series up to the limit
result = fibonacci_series(limit)

# Print the result
print("Fibonacci series up to", limit, ":", result)
