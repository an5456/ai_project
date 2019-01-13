def convert(s, numRows):
    if numRows == 1 and numRows >= len(s):
        return s
    li = [[] for x in range(numRows)]
    row, step = 0, 1
    for i in s:
        li[row].append(i)
        if row == 0:
            step = 1
        elif row == numRows - 1:
            step = -1
        row += step
    result = ''
    for y in range(len(li)-1):
        result = result+''.join(li[y])
    return result


s = convert("PAYPALISHIRING", 4)
print(s)
