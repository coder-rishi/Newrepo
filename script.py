print("hello world")

def add():
    global x, y
    x = int(input("type one number: "))
    y = int(input("type second number: "))
    return str(x+y)

print("\n", add()*(x+y), "\n")