count = int(input())
list = []
for i in range(count):
    num = int(input())
    list.append(num)
list.sort()
sum = 0
sum1 = 0
if count%2 == 0:
    for i in range(0, len(list)-1, 2):
        sum = sum + list[i+1] - list[i]
else:
    for i in range(0, len(list)-1, 2):
        sum = sum + list[i+1] - list[i]
    for i in range(len(list) - 1, 1, -2):
        sum1 = sum1 + abs(list[i] - list[i-1])

print(count//2, min(sum,sum1))
