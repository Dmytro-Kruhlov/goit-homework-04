

def logged_func(func):

    def wrapper(*args, **kwargs):

        print(f'called with {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'result: {result}')
        return result
    
    return wrapper

@logged_func
def hello():
    print("hello")


@logged_func
def hello_name(name):
    print(f"Hello {name}")
    return name

@logged_func
def summ(x, y, z):
    return x + y + z


summa = summ(5, 3, z=12)
hello()

print(summa)
hello_name("Vasya")
hello_name(name="Oleg")