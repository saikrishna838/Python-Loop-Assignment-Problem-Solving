m = int(input())
n = int(input())
previous_product = 1
for i in range(m, n + 1):
    if (i % 3) == 0:
        previous_product = previous_product * i
print(previous_product)