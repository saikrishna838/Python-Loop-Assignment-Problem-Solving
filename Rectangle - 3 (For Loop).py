m = int(input())
n = int(input())

for i in range(1, (m + 1)):
    if n > m:
        result = (str(i) + " ") * n
        print(result)
    if m > n:
        result = (str(i) + " ") * n
        print(result)