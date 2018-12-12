def add():
	global count
	count=0
	count=count + 1

def display():
    print("count= " + str(count) )
	
if __name__ == '__main__':
	add()
	display()