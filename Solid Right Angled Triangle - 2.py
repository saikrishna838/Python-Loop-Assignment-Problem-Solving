n = int(input())
count1 = 0
count2 = 0
for i in range(n * 2):
    if i < n:
        count1 = i + 1
        star = "* " * count1
        print(star)
    if i >= n  and i < (n * 2):
        count2 = count2 + 1
        star = "* " * count2
        print(star)
        