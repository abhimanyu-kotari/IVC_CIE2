# Program to calculate sum of digits

n = int(input("Enter number: "))
digit_sum = 0

while n > 0:
    digit = n % 10
    digit_sum += digit
    n = n // 10

print("Sum of digits:", digit_sum)