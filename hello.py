import sys
def hello():
	if sys.argv[1] == "Mars":
		hellomars()
	elif sys.argv[1] == "Jupiter":
		hellojupiter()
	else:
		helloworld()

def hellomars():
	print('Hello mars!')

def helloworld():
	print("Hello world!")


def hellojupiter():
	print('Hellojupiter')

if __name__ == '__main__':
	hello()

