array = [list(map(int, input().split())) for _ in range(10)]

x, y = 1,1

while True:
    if (array[x][y] == 0):
        array[x][y] = 9
    elif (array[x][y] == 2):
        array[x][y] = 9
        break

    if ((array[x][y+1] == 1 and array[x+1][y] == 1)):
        break

    if (array[x][y+1] != 1):
        y += 1
    elif (array[x+1][y] != 1):
        x += 1

for i in range(10):
    for j in range(10):
        print(array[i][j], end=' ')
    print()