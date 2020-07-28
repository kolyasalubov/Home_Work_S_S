def sorter(textbooks):
    #Cramming before a test can't be that bad?
    textbooks = sorted(textbooks, key = str.lower)
    return textbooks