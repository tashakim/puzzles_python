file = open("sample_text.txt", "w")
#f.truncate(10)
file.truncate()
file.close()

#opens and reads the file after the truncate:
file = open("sample_text.txt", "r")
print(f.read())

