n = int(input())

for i in range(1, n + 1):
    spaces = n - i
    nums = str(i) + " "
    row = " " * spaces + nums * i
    print(row)
for i in range(1, n):
    spaces = i
    nums = n - i
    row = " " * spaces + (str(nums) + " ")  * nums
    print(row)