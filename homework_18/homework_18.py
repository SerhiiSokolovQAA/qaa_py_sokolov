def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)

def fibonacci_sequence(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for num in fibonacci_sequence(21):
    print(num)

class ReverseListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]

for item in ReverseListIterator([1, 2, 3]):
    print(item)

class EvenRange:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                val = self.current
                self.current += 1
                return val
            self.current += 1
        raise StopIteration

for num in EvenRange(7):
    print(num)

def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Call {func.__name__} with args {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Result: {result}")
        return result
    return wrapper

@log_arguments_and_result
def add(x, y):
    return x + y

add(3, 4)

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] in function {func.__name__} appeared an error: {e}")
            return None
    return wrapper

@handle_exceptions
def divide(x, y):
    return x / y

print(divide(10, 2))
print(divide(10, 0))
