class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        return moves.count('U')==moves.count('D') and moves.count('R')==moves.count('L')



if __name__ == '__main__':
    s = Solution()
    print(s.judgeCircle('UDLDLD'))

