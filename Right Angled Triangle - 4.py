n = int(input())
count1 = 0
count2 = 0
for i in range( n * 2):
    if i < n:
        count1 = count1 + 1
        result = "* " * count1
        print(result)
    else:
        count2 = count2 + 1
        result = "* " * count2
        print(result)
