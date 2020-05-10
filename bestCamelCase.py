def to_camel_case(text):
    #your code here
    return text[:1]+text.title()[1:].replace("-", "").replace("_", "")

s="to_camel_case"
print(to_camel_case(s))