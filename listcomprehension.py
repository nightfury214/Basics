tmp = [x**2 for x in range(1,6)]
print(tmp)


nums = [1,2,3,4,5,6]
evens = [x for x in nums if x % 2 == 0]
print(evens)


pairs = [(x,y) for x in [1,2] for y in [3,4]]
print(pairs)