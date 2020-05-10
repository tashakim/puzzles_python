def to_camel_case(text):
  t= text.replace("_", " ")
  s = t.title()
  return s

text = "_convert_this"
print(to_camel_case(text))
str = "Hello world"
print(str.replace(" ", "_"))