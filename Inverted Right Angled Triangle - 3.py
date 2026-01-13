n = int(input())

for i in range(n):
    count = n - i
    if count == n:
        star = "* " * count
        print(star)
    else:
        star = "+ " * count
        print(star)