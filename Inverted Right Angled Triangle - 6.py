n = int(input())

for i in range(n):
    spaces = 2 * i
    stars = n - i
    row = " " * spaces + "* " * stars
    print(row)