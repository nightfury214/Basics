""" A lambdas is a small, anonymous function in python"""
add_lambda = lambda x, y:x+y
print(add_lambda(5,3))


nums = [1,2,3,4]
tmp = list(map(lambda x:x**2, nums))
print(tmp)


people = [("alice", 25), ("bob",20), ("charlie", 30)]

serted_people = sorted(people, key=lambda x:x[0])
print(serted_people)