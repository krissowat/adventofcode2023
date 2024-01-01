with open("day1.txt", 'r') as f:
    res = 0
    # for line in f:
    for id, line in enumerate(f):
        line = line.strip()
        i = 0
        while i < len(line) and not line[i].isdigit():
            i += 1
        tens = int(line[i])
        tensdig = i
        j = len(line) - 1
        while j >= i and not line[j].isdigit():
            j -= 1
        ones = int(line[j])
        onesdig = j
        digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
        for k in range(len(line)-4):
            if line[k:k+5] in digits:
                if k < tensdig:
                    tens = digits.get(line[k:k+5])
                    tensdig = k
                if k > onesdig:
                    ones = digits.get(line[k:k+5])
                    onesdig = k
            elif line[k:k+4] in digits:
                if k < tensdig:
                    tens = digits.get(line[k:k+4])
                    tensdig = k
                if k > onesdig:
                    ones = digits.get(line[k:k+4])
                    onesdig = k
            elif line[k:k+3] in digits:
                if k < tensdig:
                    tens = digits.get(line[k:k+3])
                    tensdig = k
                if k > onesdig:
                    ones = digits.get(line[k:k+3])
                    onesdig = k

        if line[-4:] in digits:
            if len(line) - 4 > onesdig:
                ones = digits.get(line[-4:])
                onesdig = len(line) - 4
            if len(line)- 4 < tensdig:
                tens = digits.get(line[-4:])
                tensdig = len(line) - 4
        elif line[-3:] in digits:
            if len(line) - 3 > onesdig:
                ones = digits.get(line[-3:])
                onesdig = len(line)-3
            if len(line) - 3 < tensdig:
                tens = digits.get(line[-3:])
                tensdig = len(line) - 3
        elif line[-4:-1] in digits:
            if len(line) - 4 > onesdig:
                ones = digits.get(line[-4:-1])
            if len(line) - 4 < tensdig:
                tens = digits.get(line[-4:-1])
        res += 10*tens + ones
        print(line.strip(), tens, ones, res)
    print(res)
        


