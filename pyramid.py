def fullPyramid():
    for i in range(5):
        for s in range(5, i+1, -1):
            print(end=" ")
        for j in range(i + 1):
            print(end="* ")
        print()
def invertedFullPyramid():
    for i in range(5):
        for s in range(i):
            print(end=" ")
        for j in range(i, 5):
            print(end="* ")
        print()
fullPyramid()
invertedFullPyramid()
