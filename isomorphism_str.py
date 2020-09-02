class Isomorphism:
	def wordPattern(self, pattern, strings):
		"""Purpose: Return whether or not there is 
		a bijection between a letter in pattern, 
		and a non-empty word in strings.
		"""
		unique_chars_in_pattern = len(set(pattern))
		unique_words_in_strings = len(set(strings.split(" ")))
		unique_pairs = len(set(zip(pattern, strings.aplit(" "))))		
		return unique_chars_in_pattern == unique_words_in_strings == unique_pairs
		

	def stringPattern(self, p, q):
		"""Purpose: Return whether or not the characters
		in p can be replaced to get q.
		
		Example: 
		p, q = "paper", "adame" => True
		p, q = "hey", "boo" => False
		"""
		unique_chars_in_p = len(set(p))
		unique_chars_in_q =  len(set(q))
		unique_pairs_in_pq = len(set(zip(p,q)))
		return unique_chars_in_q == unique_chars_in_p == unique_pairs_in_pq
