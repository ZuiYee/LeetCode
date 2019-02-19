class Solution:
    def selfDividingNumbers(self, left: 'int', right: 'int') -> 'List[int]':
        lis = []
        for i in range(left, right+1):
            j = i
            flag = 0
            while j:
                k = j
                j, p = divmod(j, 10)
                if p == 0 :
                    flag = 1
                    break
                if not i % p == 0:
                    flag = 1
                    break
            if not flag:
                lis.append(i)
        return lis


import time

def run(*args):
    s = Solution()
    start = time.time()
    print(s.selfDividingNumbers(*args))
    end = time.time()
    print(end-start)

if __name__ == '__main__':
    left = 1
    right = 22
    run(left, right)

