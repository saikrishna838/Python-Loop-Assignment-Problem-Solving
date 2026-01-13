x = int(input())
n = int(input())
total_sum = 0
for i in range(n):
    power = 2 * i + 1
    term = x ** power
    if i % 2 != 0:
        term = -term
    total_sum = total_sum + term
print(total_sum)