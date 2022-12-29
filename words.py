file = 'nounlist.txt'
handle = open(file)

easy = list()
hard = list()
harder = list()

for word in handle:
    if len(word.rstrip('\n')) < 4:
        easy.append(word.rstrip('\n'))
    elif len(word.rstrip('\n')) < 6:
        hard.append(word.rstrip('\n'))
    else:
        harder.append(word.rstrip('\n'))

