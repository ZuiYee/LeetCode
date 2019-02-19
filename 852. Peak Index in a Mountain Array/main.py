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





# 1 2 3 4 5  6 7 8 3 2
# 5
# 10
#
0
#  1 2 3 5 7 6 4
# 3
# 7
# 0 1 2 3 5 7 6 4 2

mid = 4
length = 9


import time

def run(object):
    s = Solution()
    start = time.time()
    print(s.peakIndexInMountainArray(object))
    end = time.time()
    print(end-start)

if __name__ == '__main__':
    A = [0,1,0]
    B = [0,2,1,0]
    C = [1, 2, 3, 4, 5, 6, 7, 8, 3, 2]
    run(A)
    run(B)
    run(C)
