count = int(input())

num = input().split()

for i in range(count):
    num[i] = int(num[i])

d = []
for i in range(24):
    d.append(0)

for i in range(count):
    d[num[i]] += 1

for i in range(1,24):
    print(d[i], end=' ')