""" 2048 - Game"""

import random


def startGame():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    return mat


def addNew2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2


def getCurrentStatus(mat):
    # Cheking is 2048 present in matrix
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "WON"

    # Cheking if there exists any 0 in the matrix or not
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return "Game Not Over Yet"

    # Cheking in 3x3 matrix
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i + 1][j]) or (mat[i][j] == mat[i][j + 1]):
                return "Game Not Over Yet"

    # Cheking the last row
    for i in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return "Game Not Over Yet"

    # Checking the last column
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return "Game Not Over Yet"

    # Returning Game Over
    return "Game - Over"


def compress(mat):
    newMat = []
    changed = False
    for i in range(4):
        newMat.append([0] * 4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                newMat[i][pos] = mat[i][j]
                pos += 1
                if j != pos:
                    changed = True
    return newMat, changed


def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                changed = True
                mat[i][j] = 2 * mat[i][j]
                mat[i][j + 1] = 0
    return mat, changed


def reverseMat(mat):
    newMat = []
    for i in range(4):
        newMat.append([])
        for j in range(4):
            newMat[i].append(mat[i][4 - j - 1])

    return newMat


# My own logic
def reverse(mat):
    for i in range(4):
        mat[i] = mat[i][::-1]
    return mat


def transpose(mat):
    newMat = []
    for i in range(4):
        newMat.append([])
        for j in range(4):
            newMat[i].append(mat[j][i])
    return newMat


def leftMove(mat):
    newMat, change1 = compress(mat)
    newMat, change2 = merge(newMat)
    newMat, temp = compress(newMat)
    changed = change1 or change2
    return newMat, changed


def rightMove(mat):
    newMat = reverseMat(mat)
    newMat, change1 = compress(newMat)
    newMat, change2 = merge(newMat)
    newMat, temp = compress(newMat)
    changed = change1 or change2
    newMat = reverseMat(newMat)
    return newMat, changed


def upMove(mat):
    newMat = transpose(mat)
    newMat, change1 = compress(newMat)
    newMat, change2 = merge(newMat)
    changed = change1 or change2
    newMat, temp = compress(newMat)
    newMat = transpose(newMat)
    return newMat, changed


def downMove(mat):
    newMat = transpose(mat)
    newMat = reverse(newMat)
    newMat, change1 = compress(newMat)
    newMat, change2 = merge(newMat)
    changed = change1 or change2
    newMat, temp = compress(newMat)
    newMat = reverse(newMat)
    newMat = transpose(newMat)
    return newMat, changed


def printMat(mat):
    print("_" * 20)
    for el in mat:
        for li in el:
            print(li, end=" ")
        print()


"""

# Testing the whole code
mat = startGame()
printMat(mat)

addNew2(mat)
printMat(mat)

addNew2(mat)
printMat(mat)

mat = upMove(mat)
printMat(mat)

mat = downMove(mat)
printMat(mat)

mat = leftMove(mat)
printMat(mat)

mat = rightMove(mat)
printMat(mat)

addNew2(mat)
printMat(mat)

mat = leftMove(mat)
printMat(mat)

mat = downMove(mat)
printMat(mat)

"""
