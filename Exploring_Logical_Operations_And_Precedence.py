# Task 1: Validating Calculations

# No parenthesis
result_no_parentheses = 5 + 2 * 3

# With parenthesis
result_with_parentheses = (5 + 2) * 3

# Result comparison
if result_no_parentheses == result_with_parentheses:
    print("The results match!")
else:
    print("The results do not match:")
    print("Result without parentheses:", result_no_parentheses)
    print("Result with parentheses:", result_with_parentheses)