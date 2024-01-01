# Part 1
with open('day2.txt', 'r') as f:
    counter = 0
    for line in f:
        line = line.strip()
        seps = line.split(':')
        rounds = seps[1].split(';')
        is_valid = True
        for round in rounds:
            cubemap = {'red': 0, 'blue': 0, 'green': 0}
            cubes = round.split(',')
            for cube in cubes:
                cube = cube.strip()
                number, color = cube.split(' ')
                cubemap[color] = int(number)
            if cubemap.get('red') > 12 or cubemap.get('green') > 13 or cubemap.get('blue') > 14:
                is_valid = False
        if is_valid:
            counter += int(seps[0].split(' ')[1])
    print(counter)

# Part 2
with open('day2.txt', 'r') as f:
    counter = 0
    for line in f:
        line = line.strip()
        seps = line.split(':')
        rounds = seps[1].split(';')
        is_valid = True
        cubemap = {'red': 0, 'blue': 0, 'green': 0}
        for round in rounds:
            cubes = round.split(',')
            for cube in cubes:
                cube = cube.strip()
                number, color = cube.split(' ')
                cubemap[color] = max(cubemap.get(color), int(number))
        product = 1
        for value in cubemap.values():
            product *= value
        counter += product
    print(counter)

