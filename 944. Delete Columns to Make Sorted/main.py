class Solution:
    def minDeletionSize(self, A: 'List[str]') -> 'int':
        # A_element_len = len(A[0])
        # flag = 0
        # for i in range(0, A_element_len):
        #     des = True
        #     for j in range(0, len(A)-1):
        #         # print(A[j][i], A[j+1][i])
        #         if A[j][i] > A[j+1][i]:
        #             des = False
        #             break
        #     if not des:
        #         flag += 1
        # return flag
        count = 0
        for col in zip(*A):
            if any(col[i] > col[i+1] for i in range(len(col) - 1)):
                count += 1
        return count

import time

def run(object):
    s = Solution()
    start = time.time()
    print(s.minDeletionSize(object))
    end = time.time()

if __name__ == '__main__':
    A = ["cba","daf","ghi"]
    B = ["a","b"]
    C = ["zyx","wvu","tsr"]
    run(A)
    run(B)
    run(C)
