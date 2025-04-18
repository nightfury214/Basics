value = 1 #global namespace

def func():
	value = 2 #local namespace
	def func2(): 
		value=3 #local namespace
	func2()

func() # local namespace
print(value) #global namespace



x = 5 #global namespace
def my_func():
	x = 10 #local namespace
	print(x)

my_func() # local namespace
print(x) # global namespace