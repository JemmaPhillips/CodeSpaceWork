# generate multiplication table
def multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# Get input
number = int(input("Enter a number: "))

# generate the multiplication table
multiplication_table(number)
