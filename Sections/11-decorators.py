from functools import wraps


def my_personal_decorator(func):
    # preserves the identity of the original function
    # print_my_personal_name in this case
    @wraps
    def wrapper(*args, **kwargs):
        print(f"{'hello world':_^20}")
        result = func(*args, **kwargs)
        print(f"{'bye world':_^20}")
        return result

    return wrapper


@my_personal_decorator
def print_my_personal_name():
    print("abood")

# => this syntax is equivalent to
# print_my_personal_name = my_personal_decorator(print_my_personal_name)

# practice1


def repeat(num_times):
    def repeat_decorator(func):
        @wraps
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
            # you can return the result if there is an output from the function
        return wrapper
    return repeat_decorator


@repeat(num_times=5)
def print_name(name):
    print(f"Hello {name}")


print("abood")

# practice 2


def decorator_1(func):
    def wrapper(*args, **kwargs):
        print("First decorator declared")
        result = func(*args, **kwargs)
        print("First decorator ended")
        return result
    return wrapper


def decorator_2(func):
    def wrapper(*args, **kwargs):
        print("Second decorator declared")
        result = func(*args, **kwargs)
        print("Second decorator ended")
        return result
    return wrapper


@decorator_1
@decorator_2
def add_number(n1):
    return n1


addition = add_number(2)
print(addition)
