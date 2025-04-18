tmp = {x:x**2 for x in range(5)}
print(tmp)


original = {'a': 1, 'b': 2, 'c': 3}
filtered = {k:v for k, v in original.items() if v > 1}
print(filtered)


words = ['apple', 'banana', 'cherry']
lengths = {word:len(word) for word in words}
  