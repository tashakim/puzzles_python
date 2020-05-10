def to_camel_case(text):
    #your code here
    if(len(text) == 0):
        return text
    bool = False
    if(text[0].islower()):
        bool = True
        
    t = text.replace("_", " ")
    t = t.replace("-",  " ")
    ret = t.title()
    ret2 = ret.replace(" ", "")
    if(bool == True):
          ret2 = ret2[0].lower() + ret2[1:]

    return ret2

