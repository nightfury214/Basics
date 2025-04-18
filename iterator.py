"""iterators let you loop through items one at a time"""

class Countdowned:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

# Use the class-based iterator
for num in Countdowned(5):
    print(num)



for i in [1,2,3]:
    print("no:", i)

it = iter([1,2,3])
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break


class BookReader:
    def __init__(self, pages):
        self.pages = pages
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < len(self.pages):
            page = self.pages[self.current]
            self.current += 1
            return page
        else:
            raise StopIteration
        
books = ["one", "two", "three", "four", "five"]   
render = BookReader(books)

for page in render:
    print(page)