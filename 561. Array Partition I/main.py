class Solution:
    def arrayPairSum(self, nums: 'List[int]') -> 'int':
        sum = 0
        nums.sort()
        for num in nums[::2]:
            sum += num
        return sum

import timeit

def run(*args):
    s = Solution()
    print(s.arrayPairSum(*args))

def test_loop(*args):
    run(A)

if __name__ == '__main__':
    A = [1,4,3,2]

    test_loop(A)


    t = timeit.Timer("test_loop", setup="from __main__ import test_loop")

    print("Loop:", t.timeit())

