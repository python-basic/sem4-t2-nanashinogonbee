import time

def benchmark(func):
    def wrapper():
        start = time.perf_counter()
        func()
        print('execution time: {}'.format(time.perf_counter() - start))
    return wrapper


@benchmark
def my_func():
    print([x ** 2 for x in range(50)])


print(my_func())

