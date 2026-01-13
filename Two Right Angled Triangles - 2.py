n = int(input())
count1 = 0 
count2 = 0
for i in range( n * 2):
    if i < n:
        count1 = count1 + 1
        star = "* " * count1
        print(star)
    if i >= n and i <= (n * 2):
        star = n - count2
        star = "* " * star
        count2 = count2 + 1
        print(star)
    