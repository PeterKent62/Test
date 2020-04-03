import random


def cached(func):
    value = 0
    prev_args = []
    same_args = False

    def wrapper(*args):
        print(f'Summing {args} ...')
        nonlocal value, prev_args, same_args

        if prev_args == args:
            print('Already counted!')
            same_args = True
        else:
            same_args = False
            value = func(*args)
            print('Completed!')
            prev_args = args[:]

        return value, same_args

    return wrapper


@cached
def sum_func(*args):
    s = 0

    for i in args:
        s += i

    return s


# for i in range(3):
#     print(sum_func(*[i for i in range(1, random.randint(1, 30))]))

print(sum_func()[0], '\n')

print(sum_func(1, 2, 3)[0], '\n')
print(sum_func(1, 2, 3)[0], '\n')

print(sum_func(2)[0], '\n')
print(sum_func(2, 3)[0], '\n')

print(sum_func(2, 3)[0], '\n')
print(sum_func(3, 2)[0], '\n')
