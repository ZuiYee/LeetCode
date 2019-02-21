class Solution:
    def fib(self, N: 'int') -> 'int':
        f = lambda x: x if x <= 2 else f(x - 1) + f(x - 2)
        return f(N)
