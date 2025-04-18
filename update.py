import time

test_set = set()

"""add operation"""
start_time = time.time()
for i in range(1000000):
    test_set.add(i)
end_time = time.time()
print(f"add operation:{end_time - start_time: .6f} seconds")


"""remove operation"""
start_time = time.time()
for i in range(1000000):
    test_set.remove(i)
end_time = time.time()
print(f"remove operation:{end_time - start_time: .6f} seconds")

def func(value, ls=[]):
	ls.append(value)
	print(ls)

func(1)
func(2)
func(3, [])
func(4)
