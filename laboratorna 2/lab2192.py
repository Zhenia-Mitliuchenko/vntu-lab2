column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())

if abs(column1 - column2) == abs(row1 - row2) and (column1, row1) != (column2, row2):
    print("Yes")
else:
    print("No")
    