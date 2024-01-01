# Part 1
with open('day3.txt', 'r') as f:
    matrix = [['x']*140 for x in range(140)]
    for i, line in enumerate(f):
        line = line.strip()
        for j, c in enumerate(line):
            matrix[i][j] = c
    
    res = 0
    for i in range(len(matrix)):
        previsnum = False
        touchingsymbol = False
        numstr = ''
        for j in range(len(matrix[0])):
            # Check if number:
            if matrix[i][j].isdigit():
                numstr += matrix[i][j]
                previsnum = True
                
                #Check surrounding symbols
                if j-1 > 0:
                    if not matrix[i][j-1].isdigit() and matrix[i][j-1] != '.':
                        touchingsymbol = True
                if j+1 < len(line):
                    if not matrix[i][j+1].isdigit() and matrix[i][j+1] != '.':
                        touchingsymbol = True
                if i-1 > 0:
                    if not matrix[i-1][j].isdigit() and matrix[i-1][j] != '.':
                        touchingsymbol = True
                    if j-1 > 0:
                        if not matrix[i-1][j-1].isdigit() and matrix[i-1][j-1] != '.':
                            touchingsymbol = True
                    if j+1 < len(line):
                        if not matrix[i-1][j+1].isdigit() and matrix[i-1][j+1] != '.':
                            touchingsymbol = True
                if i+1 < len(line):
                    if not matrix[i+1][j].isdigit() and matrix[i+1][j] != '.':
                        touchingsymbol = True
                    if j-1 > 0:
                        if not matrix[i+1][j-1].isdigit() and matrix[i+1][j-1] != '.':
                            touchingsymbol = True
                    if j+1 < len(line):
                        if not matrix[i+1][j+1].isdigit() and matrix[i+1][j+1] != '.':
                            touchingsymbol = True
                
                if j + 1 == len(line):
                    if touchingsymbol:
                        res += int(numstr)
            else:
                if previsnum and touchingsymbol:
                    res += int(numstr)
                touchingsymbol = False
                numstr = ''
                previsnum = False
    print(res)


# Part 2
with open('day3.txt', 'r') as f:
    matrix = [['x']*140 for x in range(140)]
    for i, line in enumerate(f):
        line = line.strip()
        for j, c in enumerate(line):
            matrix[i][j] = c
    
    gears = {}
    for i in range(len(matrix)):
        previsnum = False
        touchingsymbol = False
        symbols = set()
        numstr = ''
        for j in range(len(matrix[0])):
            # Check if number:
            if matrix[i][j].isdigit():
                numstr += matrix[i][j]
                previsnum = True
                
                #Check surrounding symbols
                if j-1 > 0:
                    if matrix[i][j-1] == '*':
                        touchingsymbol = True
                        symbols.add((i, j-1))
                if j+1 < len(line):
                    if matrix[i][j+1] == '*':
                        touchingsymbol = True
                        symbols.add((i, j+1))
                if i-1 > 0:
                    if matrix[i-1][j] == '*':
                        touchingsymbol = True
                        symbols.add((i-1, j))
                    if j-1 > 0:
                        if matrix[i-1][j-1] == '*':
                            touchingsymbol = True
                            symbols.add((i-1, j-1))
                    if j+1 < len(line):
                        if matrix[i-1][j+1] == '*':
                            touchingsymbol = True
                            symbols.add((i-1, j+1))
                if i+1 < len(line):
                    if  matrix[i+1][j] == '*':
                        touchingsymbol = True
                        symbols.add((i+1, j))
                    if j-1 > 0:
                        if matrix[i+1][j-1] == '*':
                            touchingsymbol = True
                            symbols.add((i+1, j-1))
                    if j+1 < len(line):
                        if matrix[i+1][j+1] == '*':
                            touchingsymbol = True
                            symbols.add((i+1, j+1))
                
                if j + 1 == len(line):
                    if touchingsymbol:
                        for symbol in symbols:
                            arr = gears.get(symbol, [])
                            arr.append(int(numstr))
                            gears[symbol] = arr
            else:
                for symbol in symbols:
                    arr = gears.get(symbol, [])
                    arr.append(int(numstr))
                    gears[symbol] = arr
                touchingsymbol = False
                numstr = ''
                previsnum = False
                symbols = set()
    res = 0
    for gear in gears:
        if len(gears.get(gear)) == 2:
            res += gears.get(gear)[0] * gears.get(gear)[1]
    print(res)