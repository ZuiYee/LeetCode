class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(a*a for a in A)


if __name__ == '__main__':
    s = Solution()
    a = [-4,-1,0,3,10]
    b = [-7,-3,2,3,11]
    print(s.sortedSquares(a))
    print(s.sortedSquares(b))