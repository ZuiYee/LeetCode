
class Solution:
    def peakIndexInMountainArray(self, A: 'List[int]') -> 'int':
        left, right = 0, len(A)-1
        while left<right:
            mid = (left + right)//2
            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid




import time
import timeit

def run(object):
    s = Solution()
    print(s.peakIndexInMountainArray(object))


if __name__ == '__main__':
    A = [0,1,0]
    B = [0,2,1,0]
    C = [1, 2, 3, 4, 5, 6, 7, 8, 3, 2]


    def test_loop():
        run(C)

    t = timeit.Timer("test_loop", setup="from __main__ import test_loop")

    print("Loop:", t.timeit())

