#Get numbers
first_num = float(input("Input First Number: "))
second_num = float(input("Input Second Number: "))
third_num = float (input ("Input Third Number: "))

#results
if first_num < second_num < third_num:
    print("Increasing order")
elif first_num != second_num != third_num != first_num:
    print("Decreasing order")
else:
    print("Neither increasing nor decreasing order")