m = int(input())
n = int(input())
previous_sum = 1
for i in range (m, n + 1):
    product = previous_sum * i
    previous_sum = product
print(product)