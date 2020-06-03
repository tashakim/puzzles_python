import string

def is_pangram(s):
    s= s.lower()
    n =  sorted(s.replace(" ", ""))
    s="".join(sorted(set(n), key = n.index))
    if(s.find("abcdefghijklmnopqrstuvwxyz") >= 0):
        return True
    return False