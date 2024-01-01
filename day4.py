# Part 1
total = 0
with open('day4.txt', 'r') as f:
    for line in f:
        line = line.strip()
        seps = line.split(':')
        numbers = seps[1].split('|')
        winning_nums = numbers[0].split(' ')
        card_nums = numbers[1].split(' ')
        points = 0
        for number in card_nums:
            if number != '' and number in winning_nums:
                if points == 0:
                    points = 1
                else:
                    points*=2
        total += points
print(total)

# Part 2
