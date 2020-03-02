def gcov(path, f_lines=None):
    hits = {}
    with open(path, 'r') as f:
        for line in f:
            if line.startswith("function"):
                if f_lines is not None:
                    function = line.split()[1]
                    f_lines[function] = []
                continue
            elif line.startswith("branch"):
                continue
            count, number = line.split(':')[0].strip(), int(line.split(':')[1].strip())
            if number < 1 or count == '-':
                continue
            if f_lines is not None and function is not None:
                f_lines[function].append(number)
            hits[number] = 0 if count=='#####' else int(count)
    return hits
