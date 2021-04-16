# 初始化棋盘
def InitialChckerBoard(row, col):
    Cboard = [['[ ]' for i in range(col)] for j in range(row)]
    for i in range(row):
        Cboard[0][i] = str(i).center(3)
    for i in range(col):
        Cboard[i][0] = str(i).rjust(3)
    return Cboard


# 显示棋盘
def DisplayCheckerBoard(Cboard):
    for i in range(n):
        for j in range(m):
            print(Cboard[i][j], end='  ')
        print()
    print()


# 判断此处是否有子
def CheckPiece(x, y):
    if Cboard[x][y] == ' * ' or Cboard[x][y] == ' o ':
        return True
    return False


# 下棋
def MakeMove(Cboard):
    global Move, m1, m2
    if CheckPiece(Move[1], Move[2]) == False:
        if Move[0] == 1:
            mark = ' * '
            m1 += 1
            Move[0] = 2
            print('Player1 put the ', m1, ' piece at (', Move[1], ', ', Move[2], ').')
        else:
            mark = ' o '
            m2 += 1
            Move[0] = 1
            print('Player2 put the ', m2, ' piece at (', Move[1], ', ', Move[2], ').')
        Cboard[Move[1]][Move[2]] = mark
        return Cboard
    else:
        print('To player', Move[0], ': please re-select location!')
        return Cboard


# 自动选择下棋位置
def SelectPointA(row,col):
    Move[1] = random.randint(1, row-1)
    Move[2] = random.randint(1, col-1)


# 人工选择下棋位置
def SelectPointP(row, col):
    Move[1] = row
    Move[2] = col


# 判断输赢
def CheckResult(Cboard):
    global winner
    for i in range(1, n - 4):
        for j in range(1, m - 4):
            if Cboard[i][j] == ' * ' or Cboard[i][j] == ' o ':
                if Cboard[i][j] == ' * ':
                    winner = 1
                else:
                    winner = 2
                if Cboard[i + 1][j] == Cboard[i][j]:  # 判断同一行是否连成5个
                    for k in range(1, 4):
                        if Cboard[i + 1 + k][j] != Cboard[i][j]:
                            break
                        else:
                            if k == 3:
                                return True
                if Cboard[i][j + 1] == Cboard[i][j]:  # 判断同一行是否连成5个
                    for k in range(1, 4):
                        if Cboard[i][j + 1 + k] != Cboard[i][j]:
                            break
                        else:
                            if k == 3:
                                return True
                if Cboard[i + 1][j + 1] == Cboard[i][j]:  # 判断左上-右下对角是否连成5个
                    for k in range(1, 4):
                        if Cboard[i + 1 + k][j + 1 + k] != Cboard[i][j]:
                            break
                        else:
                            if k == 3:
                                return True
                if j > 4:
                    if Cboard[i + 1][j - 1] == Cboard[i][j]:  # 判断右上-左下对角是否连成5个
                        for k in range(1, 4):
                            if Cboard[i + 1 + k][j - 1 - k] != Cboard[i][j]:
                                break
                            else:
                                if k == 3:
                                    return True
    return False


# 判断棋盘是否下满
def CheckFull(Cboard):
    for i in range(1, n):
        for j in range(1, m):
            if Cboard[i][j] != ' * ' and Cboard[i][j] != ' o ':
                return False
    return True


if __name__ == '__main__':
    # 主进程
    import random

    m = 21
    n = 21
    # 创建（m-1）*（n-1）的棋盘
    Cboard = InitialChckerBoard(m, n)
    DisplayCheckerBoard(Cboard)

    #声明下棋落点的全局变量
    global Move, m1, m2, winner
    Move = [1, 3, 3]
    m1 = 0
    m2 = 0

    mode = input("Please choose the game mode(a:auto,p:people):a/p:")
    if mode == 'a':
        while (CheckResult(Cboard) == False) and (CheckFull(Cboard) == False):
            SelectPointA(m,n)
            Cboard = MakeMove(Cboard)
            DisplayCheckerBoard(Cboard)
    elif mode == 'p':
        while (CheckResult(Cboard) == False) and (CheckFull(Cboard) == False):
            print('Player', Move[0], ': row <= ', m - 1, ' column <= ', n - 1)
            inrow = int(input('Enter the row:'))
            incol = int(input('Enter the column:'))
            SelectPointP(inrow, incol)
            Cboard = MakeMove(Cboard)
            DisplayCheckerBoard(Cboard)

    # 判断棋局结果
    if CheckResult(Cboard) == True:
        print('Player', winner, 'won the game!')
    if CheckFull(Cboard) == True:
        print('Draw')

