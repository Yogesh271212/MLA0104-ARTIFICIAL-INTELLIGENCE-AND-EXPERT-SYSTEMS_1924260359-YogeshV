def sum_natural_numbers(n):
    if n <= 1:
        return n
    return n + sum_natural_numbers(n - 1)

number = 10
total = sum_natural_numbers(number)
print(f"Sum of natural numbers from 1 to {number} is: {total}")
