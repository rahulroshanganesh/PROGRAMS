#CHECK IF THE GIVEN MATRIX IS MAGIC SQUARE OR NOT 
# We define a magic square to be an nxn matrix of distinct positive integers from 1 to n^2 where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.
from icecream import ic
# s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
s =[[4 ,9 ,2],[3 ,5 ,7],[8 ,1 ,6]]
# print(s)
res = 0
res1 = 0
row = []
column = []
for i in range(0, len(s)):
    for j in range(0, len(s[i])):
        res = res + s[i][j]
        res1 = res1 + s[j][i]
    # ic(res)
    row.append(res)
    # ic(res1)
    column.append(res1)
    res = 0
    res1 = 0

# ic(row)
# ic(column)

len_res = list(set(row))
len_res = len(len_res)
len_res1 = list(set(column))
len_res1 = len(len_res1)
if len_res == 1 and len_res1 == 1:
    print("It is a magic square")
else:
    print("No it is not magic square")