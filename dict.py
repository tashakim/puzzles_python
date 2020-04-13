def makedict(**args):
	return args

def  dodict(*args, **kwds):
	d = {}
	for k, v in args: d[k] = v
	d.update(kwds)
	return d

if __name__ == "__main__":
	data = makedict(red = 1, blue = 2, green = 3)
	data2 = dodict(*data.items(), yellow = 2, green = 4)
