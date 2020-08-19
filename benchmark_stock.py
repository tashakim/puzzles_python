def benchMark(input_string):		
	"""Purpose: Returns the transactions necessary to make a portfolio match 
	a benchmark. 
	Note: Shares are positive decimals. There are at least 1 asset present in 
	Portfolio and Benchmark. Trades should be sorted in alphabetical order based on 
	the names of the assets.
	"""
	def sortAssets(input_string):
		"""Purpose: This is a helper method that parses the 
		input string, then stores given assets into appropriate portfolios.
		Time Complexity: Sorting is done in O(n) linear time.
		"""
		parts = input_string.split(':')
		portfolio = parts[0].split('|')
		benchmark = parts[1].split('|') 

		for item in portfolio:
			t = item.split(',')
			part = t[0] + ","+t[1]
			portfolio_list[part] = t[2]

		for item in benchmark:
			t = item.split(',')
			part = t[0] + "," + t[1]
			benchmark_list[part] = t[2]
			
		return

	portfolio_list = {} # Hash Table to store assets in current Portfolio
	benchmark_list = {} # Hash Table to store assets in benchmark Portfolio

	sortAssets(input_string) # stores each asset by Name, Type, and Number

	transactions = [] # Initialize array to store ultimate list of transactions
	for k,v in benchmark_list.items():

		if k in portfolio_list:
			if v > portfolio_list[k]: 
				# if number of shares in benchmark is larger, we must "BUY"
				difference = int(v) - int(portfolio_list[k])
				transaction = "BUY," + k + "," + str(difference)
			elif v < portfolio_list[k]:
				# if number of shares in benchmark is smaller, we must "SELL"
				difference = int(portfolio_list[k]) - int(v)
				transaction = "SELL," + k + "," + str(difference)
			else:
				# if number of shares in benchmark equals that in our current portfolio, 
				# NO TRANSACTION is made.
				break
			
		elif k not in portfolio_list:
			transaction = "BUY," + k + "," + v
		transactions.append(transaction)
	
	for k, v in portfolio_list.items():
		if k not in benchmark_list:
			transactions.append("SELL" + k + "," + v)

	# Output a list of transactions separated by a NEW LINE
	for i in sorted(transactions):
		print(i, end = "\n")
	return


if __name__ == "__main__":
	print("\nExample input: ")
	benchMark('Vodafone,STOCK,10|Google,STOCK,15|Microsoft,BOND,15:Vodafone,STOCK,15|Google,STOCK,10|Microsoft,BOND,15')
	print("\nTest input 1: ")	
	benchMark('Vodafone,STOCK,10|Google,STOCK,15:Vodafone,STOCK,15|Vodafone,BOND,10|Google,STOCK,10')
	print("\nTest input 2: ")
	benchMark('Vodafone,STOCK,10|Google,STOCK,15|Microsoft,BOND,15:Vodafone,STOCK,15|Google,STOCK,10|Microsoft,BOND,15')

	print("\nEnd of transactions for the day")

