def camelCase(text):
	return text[:1] + text.title()[1:].replace("_", "").replace("-", "")

print(camelCase("this_camel_case"))
print(camelCase("This_camel-case"))