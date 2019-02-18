class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = {}
        for a in A:
            try:
                if count[a]:
                    return a
            except:
                count[a] = 1


if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,3]
    b = [2,1,2,5,3,2]
    c = [5,1,5,2,5,3,5,4]
    print(s.repeatedNTimes(a))
    print(s.repeatedNTimes(b))
    print(s.repeatedNTimes(c))