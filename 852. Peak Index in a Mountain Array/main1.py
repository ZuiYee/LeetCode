class Solution:
    def peakIndexInMountainArray(self, A: 'List[int]') -> 'int':
        for i in range(len(A) - 1):
            if A[i + 1] < A[i]:
                return i
        return -1




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
