n = int(input())  #输入行
black=[]          #用来记录已染色格子的坐标，将坐标放入black中表示已染色
X = [[1 for i in range(4)] for j in range(n)] #初始化二维数组
for i in range(n):
    X[i] = list(map(int, input().split()))  #接收输入的二维数组

#循环每一行
for i in range(n):
    #两个坐标在同一行的情况
    if X[i][0] == X[i][2]:
        num = abs(X[i][1] - X[i][3]) + 1  #记录两个坐标之间有几个格子
        minX = min(X[i][1], X[i][3])      #记录两个坐标中纵坐标较小的坐标的纵坐标值
        for j in range(num):
            if [X[i][0],j+minX] not in black:
                black.append([X[i][0],j+minX])
    #两个坐标在同一列的情况
    if X[i][1] == X[i][3]:
        num = abs(X[i][0] - X[i][2]) + 1  #记录两个坐标之间有几个格子
        minX = min(X[i][0], X[i][2])      #记录两个坐标中横坐标较小的坐标的纵坐标值
        for j in range(num):
            if [j+minX,X[i][1]] not in black:
                black.append([j+minX, X[i][1]])
print(len(black))

