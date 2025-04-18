"""generator is a function that yield values one at a time"""
def count(n):
    while n > 0:
        yield n
        n -= 1

for num in count(5):
    print(num)


def mygenrator():
    yield 1
    yield 2
    yield 3

gen = mygenrator()

for val in gen:
    print(val)