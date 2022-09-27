import sys


def helloworld():
	print('Helloworld!')

def hellojupiter():
	print('Hellojupiter')

def hello():
	if sys.argv[1] == "Jupiter":
		hellojupiter()
	else:
		helloworld()

if __name__ == '__main__':
	hello()

