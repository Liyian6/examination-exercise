'''
题目如下：
在二维平面上有一个无限的网格图形，初始状态下，所有的格子都是空白的。
现在有n个操作，每个操作是选择一行或一列，并在这行或这列上选择两个端点网络，
把已这两个网格为端点的区间内的所有网格染黑（包括这两个端点）。
问经过n次操作之后，共有多少个格子被染黑，显然，在众多操作中，很容易重复染色同一个格子，
此时只计数一次。

输入：
输入第一行包含一个正整数n
接下来n行，每行四个整数，x1,y1,x2,y2,表示一个操作的两断格子坐标。
若x1=x2则是在一列上染色，若y1=y2，则是在一行上染色，保证每次操作是在一行或一列上染色

输出：
输出仅包含一个正整数，表示被染色各自的数量

样例：
输入
3
1 2 3 2
2 5 2 3
1 4 3 4

输出
8
'''
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

