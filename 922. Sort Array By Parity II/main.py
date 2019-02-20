import copy
class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        odd = 1
        even = 0
        ans = [None] * len(A)
        for a in A:
            if a % 2 == 0:
                ans[even] = a
                even += 2
            else:
                ans[odd] = a
                odd += 2

        return ans
