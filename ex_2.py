import time



def timeit(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'called with {args}, {kwargs}')
        result = func(*args, **kwargs)
        end = time.time()
        
        print(f'result: {result}, time: {end - start}')

        return result

    return wrapper

@timeit
def long_func(sleep_time):

    for i in range(sleep_time):

        print(f"sleeping: {i}")
        time.sleep(1)
    return "Misson complete" 

long_func(5)




    
