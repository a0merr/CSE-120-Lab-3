# Getting the list and multiplication number from the user
user_list = input("Enter a list of 13 numbers separated by commas: ").split(',')
user_list = [int(x) for x in user_list]
multiplication_number = int(input("Enter the multiplication number: "))

# Multiplying each element in the list by the multiplication number
multiplied_list = [num * multiplication_number for num in user_list]

# Output the results
print("Number:", user_list)
print("Multiplication Number:", multiplication_number)
print("Multiplied List:", multiplied_list)
