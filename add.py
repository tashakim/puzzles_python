def add(x,y):
	return x+y

def test():
	assert add(1,3) == 4, "Test failed"
	assert add(0,0) == 0, "Test failed"
	assert add(1,2) == 1, "Test huh" #wrong assertion!




if __name__ == "__main__":
	test()
