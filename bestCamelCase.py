def to_camel_case(text):
    # text[:1] instead of text[0] deals with null string
    return text[:1]+text.title()[1:].replace("-", "").replace("_", "")

s = "to_camel_case"
print(to_camel_case(s))