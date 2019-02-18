class Solution:
    def diStringMatch(self, S: 'str') -> 'List[int]':
        min, max = 0, len(S)
        result = []
        for s in S:
            if s == 'I':
                result.append(min)
                min += 1
            else:
                result.append(max)
                max -= 1
        result.append(min)
        return result


if __name__ == '__main__':
    s = Solution()
    A = "IDID"
    B = "III"
    C = "DDI"
    print(s.diStringMatch(A))
    print(s.diStringMatch(B))
    print(s.diStringMatch(C))
