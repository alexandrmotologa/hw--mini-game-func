from random import randint

# this MODULE contains the MAP logic
# 0 - empty
# 1 - wall
# 2 - robo
# 3 - mine
rr = 4
rc = 1

mr = randint(0, 9)
mc = randint(0, 9)

gameMap = [
    [0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,1,0,0,0,1],
    [0,0,0,0,0,1,0,0,0,1],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1],
]

gameMap[rr][rc] = 2
gameMap[mr][mc] = 3


def p( c ):
    print(c + " ", end="")

def printMap( m ):
    for ri in range(10):
        for ci in range(10):
            
            if m[ri][ci] == 0:
                p(".")
            if m[ri][ci] == 1:
                p("#")
            if m[ri][ci] == 2:
                p("R")
            if m[ri][ci] == 3:
                p("X")
        print()