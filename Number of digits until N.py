n = int(input())
total_digits = 0
for i in range(1, n + 1):
    no_of_digits = len(str(i))
    total_digits = total_digits + no_of_digits
print(total_digits)