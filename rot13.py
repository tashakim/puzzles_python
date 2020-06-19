def rot13(message):
    """Purpose: Returns a string ciphered with Rot13.
    """
    alph = "abcdefghijklmnopqrstuvwxyz"
    Alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    for i in range(len(message)):
        if(not message[i].isalpha()):
            res.append(message[i])
        if(message[i] in alph):
            res.append(alph[(alph.find(message[i])+13)%26])
        if(message[i] in Alph):
            res.append(Alph[(Alph.find(message[i])+13)%26])
    return "".join(c for c in res)
    

if __name__ == "__main__":

    assert(rot13("test") == "grfg"), "Wrong answer"
    assert(rot13("Test") == "Grfg"), "Wrong answer"
    print("Simple tests passed!")