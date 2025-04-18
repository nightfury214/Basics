try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


try:
    something_risky()
except Exception as e:
    print(f"Oops! Error: {e}")


try:
    x = 5 / 1
except ZeroDivisionError:
    print("division error!")

else:
    print("all good!")
finally:
    print("cleanup stuff here")
    