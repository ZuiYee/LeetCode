# from typing import List


class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        for a in A:
            for i in range((len(a)+1)//2):
                #  a[~i]: a[-i-1] a[len(a) - 1 - i)
                #  ~(int) = -(int) - 1

                a[i], a[~i] = a[~i] ^ 1, a[i] ^ 1
                # print(a[-i-1])
                # print(-i-1)
                # a[i] = a[-i - 1] ^ 1
                # a[-i-1] = a[i] ^ 1

        return A


if __name__ == '__main__':
    s = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    B = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(s.flipAndInvertImage(A))
    print(s.flipAndInvertImage(B))





