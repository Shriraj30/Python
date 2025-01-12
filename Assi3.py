def sum_digits_until_single_digit(n):
    while n > 9:  # Continue until n is a single digit
        n = sum(int(digit) for digit in str(n))  # Sum of digits
    return n

numbers = []
while True:
    number = input("Enter a number (or type 'done' to finish): ")
    if number.lower() == 'done':
        break
    numbers.append(int(number))

single_digit_sums = [sum_digits_until_single_digit(num) for num in numbers]

print(f"list1 = {numbers}")
print(f"list2 = {single_digit_sums}")
