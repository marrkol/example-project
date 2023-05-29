# 1. suma_listy
def suma_listy(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + suma_listy(l[1:])

l = [1, 2, 6, 4, 6]
print(suma_listy(l))

#   czy l jest puste?
#       y -> zwróć 0
#       n -> zwróć l[0] + suma_listy(lista_bez_0_elementu)

# 2. znajdz_najwiekszy_element_listy
def najwiekszy_element(l):
    if len(l) == 1:
        return l[0]
    else:
        max = najwiekszy_element(l[1:])
        return l[0] if l[0] > max else max

l = [5, 2, 9, 1, 7, 15, 20]
print(najwiekszy_element(l))

#   czy l ma 1 element?
#       y -> zwróć l[0]
#       n ->
#           czy najwiekszy_element(l[1:]) większe od l[0]?
#           y -> zwróć najwiekszy_element(l[1:])
#           n -> zwróć l[0]

# 3. silnia
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)
print(silnia(5))

#   czy n jest zerem?
#       y -> zwróć 1
#       n -> zwróć n * silnia(n-1)

# 4. ciag_fibonaciego
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(8))

#   czy n jest zerem?
#       y -> zwróć 0
#       n ->
#           czy n jest jedynką?
#           y -> zwróć 1
#           n -> zwróć fib(n-1) + fib(n-2)


# sudoku 4x4
import numpy as np

grid = [[0, 4, 3, 0],
    [0, 0, 0, 0],
    [0, 3, 0, 4],
    [0, 1, 2, 0]]


def check(row, column, number):
    global grid
    # sprawdzenie czy cyfra pojawia się w danym wierszu
    for i in range(0, 4):
        if grid[row][i] == number:
            return False

    # sprawdzenie czy cyfra pojawia się w danej kolumnie
    for i in range(0, 4):
        if grid[i][column] == number:
            return False

    # sprawdzenie czy cyfra pojawia się w danym kwadracie
    x0 = (column // 2) * 2
    y0 = (row // 2) * 2
    for i in range(0, 2):
        for j in range(0, 2):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True

# rekurencyjny algorytmy zstępujący (backtracking)
def solve():
    global grid
    for row in range(0, 4):
        for column in range(0, 4):
            if grid[row][column] == 0:
                for number in range(1, 5):
                    if check(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return

    print(np.matrix(grid))
solve()

# sudoku 9x9

grid = [[0, 0, 0, 5, 0, 0, 0, 2, 0],
        [0, 7, 0, 6, 0, 0, 0, 4, 0],
        [4, 2, 0, 0, 0, 1, 0, 9, 0],
        [0, 4, 0, 1, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 9, 0, 0, 7, 0],
        [5, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 5, 0, 0, 7],
        [0, 1, 4, 3, 0, 0, 0, 0, 8]]


def check(row, column, number):
    global grid
    # sprawdzenie czy cyfra pojawia się w danym wierszu
    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    # sprawdzenie czy cyfra pojawia się w danej kolumnie
    for i in range(0, 9):
        if grid[i][column] == number:
            return False

    # sprawdzenie czy cyfra pojawia się w danym kwadracie
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True

# rekurencyjny algorytmy zstępujący (backtracking)
def solve():
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if check(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return

    print(np.matrix(grid))
solve()
