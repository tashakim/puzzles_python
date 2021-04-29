def encrypt_this(text):
    """
    Purpose: Encrypts string of words.
    """
    words = text.split(' ')
    print(words)
    res = ''
    for word in words:
        res += encrypt(word) + ' '
    return res[:-1]
    
    
def encrypt(word):
    res = ''
    if len(word) >= 3:
        res += str(ord(word[0]))
        res += word[-1]
        res += word[2:-1]
        res += word[1]
    
    elif len(word) == 1:
        res += str(ord(word[0]))
    elif len(word) == 2:
        res += str(ord(word[0]))
        res += word[1]
    return res