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
numcards = 0
with open('day4.txt', 'r') as f:
    for line in f:
        numcards += 1
cardcount = {}
for i in range(numcards):
    cardcount[str(i)] = 1
with open('day4.txt', 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        seps = line.split(':')
        numbers = seps[1].split('|')
        winning_nums = numbers[0].split(' ')
        card_nums = numbers[1].split(' ')
        matches = 0
        for number in card_nums:
            if number != '' and number in winning_nums:
                matches += 1
        for j in range(matches):
            cardcount[str(i+j+1)] += cardcount.get(str(i))
    print(sum(cardcount.values()))