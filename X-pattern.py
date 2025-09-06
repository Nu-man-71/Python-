
rows = 7

for i in range(rows):
    for j in range(rows):
        if i == j or j == rows -1 -i:
            print("*", end="")
        else:
            print(" ",end="")
    print()