class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        #  lambda 简单函数 x函数入口
        return sorted(A, key=lambda x: x % 2)


if __name__ == '__main__':
    s = Solution()
    a = [3, 1, 2, 4]
    print(s.sortArrayByParity(a))