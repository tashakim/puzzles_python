def alphabet_position(text):
    """
    Purpose: replaces with alphabet position.
    """
    letters = [i.lower() for i in text]
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list(range(1, 27))

    dict = {}
    for i, a in enumerate(alphabets):
        dict[a] = numbers[i]
    res = ''
    for x in letters:
        if x.isalpha():
            res += str(dict[x]) + ' '
    return res[:-1]