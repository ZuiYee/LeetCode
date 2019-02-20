
def momo(func):
    cache = {}

    def warp(*args):
        print(args)
        print(cache)
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return warp

@momo
def fib(i):
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)


def main():
    print(fib(6))


if __name__ == '__main__':
    main()
