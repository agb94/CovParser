def gcov(path):
    hits = {}
    with open(path, 'r') as f:
        for line in f:
            count, number = line.split(':')[0].strip(), int(line.split(':')[1].strip())
            if number < 1 or count == '-':
                continue
            hits[number] = 0 if count=='#####' else int(count)
    return hits