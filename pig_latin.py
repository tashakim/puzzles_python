def pig_latin(text):
	"""Purpose: Moves first letter of each word to the 
	back, then adds 'ay' to the end of word. 
	Note: Leave punctuation marks untouched.
	Note2: Codewars test cases don't seem very comprehensive.
	"""
	res = ""
	for word in text.split():
		if(word != "!" and word != "?"):
			res += word[1:] + word[0] + "ay "
		if(word == "!" or word == "?"):
			res += word + " "
	return res[:-1]