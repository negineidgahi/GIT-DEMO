import sys

def hello():
	if sys.argv[1] == "Mars":
		hellomars()
	else:
		helloworld()

def hellomars():
	print('Hello mars!')

def helloworld():
	print("Hello world!")
if __name__ == '__main__':
	hello()

