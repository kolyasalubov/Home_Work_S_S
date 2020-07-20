def list_animals(animals):
    list = ''
    for v in range(len(animals)):
        list += str(v + 1) + '. ' + animals[v] + '\n'
    return list