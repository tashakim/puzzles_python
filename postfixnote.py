def postFixNote(S):
	"""Purpose: Returns the postfix notation of a numeric expression.
	"""
	stack = ArrayStack()
	answer = [] 
	for c in S:
		if(c.isalpha()):
			answer.append(c)
		elif(stack.isEmpty()):
			stack.push(c)
		else:
			if(c == '('):
				stack.push(c)
			elif(c == ')'):
				while(stack.peek() != '('):
					answer.append(stack.pop())
				stack.pop()
			elif(prec[c] > prec[stack.peek()]):
				stack.push(c)
			else:
				answer.append(stack.pop())
				stack.push(c)
	while(not stack.isEmpty()):
		answer.append(stack.pop())
	return answer