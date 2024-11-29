import time


# 是否是质数
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def test_normal():
    start = time.time()
    for i in range(1, 10000):
        is_prime(i)
    end = time.time()
    print("Time:", end - start)

test_normal()


def display_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time:", end - start)
    return wrapper

# 没有参数，没有返回值
@display_time
def test_decorator():
    for i in range(1, 10000):
        is_prime(i)
test_decorator()


# 有返回值
def display_time1(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print('Time:', end - start)
        return result
    return wrapper

@display_time1
def test_decorator1():
    count = 0
    for i in range(1, 10000):
        if is_prime(i):
            count += 1
    return count
print(test_decorator1())


# 有参数，有返回值
def display_time2(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Time:', end - start)
        return result

    return wrapper


@display_time2
def test_decorator2(max_value):
    count = 0
    for i in range(1, max_value):
        if is_prime(i):
            count += 1
    return count


print(test_decorator2(10000))
