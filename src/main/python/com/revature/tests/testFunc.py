#testFunc.py

def testFunc(a, b, func):
	return func(a, b)
	
def add(a, b):
	return a + b

def multiply(a, b):
	return a*b

def main():
	print(testFunc(4, 6, add))
	print(testFunc(4, 6, multiply))
	
if __name__=='__main__':
	main()