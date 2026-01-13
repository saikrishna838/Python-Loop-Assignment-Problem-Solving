n = int(input())
k = int(input())
number = 1
previous_sum = 0
for i in range(n):
    cube = number ** k
    sum = previous_sum + cube
    number = number +  1
    previous_sum =  sum
print(sum)
    
