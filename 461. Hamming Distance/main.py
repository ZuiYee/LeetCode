class Solution:
    def hammingDistance(self, x: 'int', y: 'int') -> 'int':
        # z = x ^ y
        # num = 0
        # while z!=0:
        #     num += z & 1
        #     print(z & 1)
        #     z >>= 1
        # return num



        hamming_distance = 0
        s = str(bin(x ^ y))
        for i in range(2, len(s)):
            if int(s[i]) is 1:
                hamming_distance += 1
        return hamming_distance


if __name__ == '__main__':
    s = Solution()
    x = 7
    y = 26
    print(s.hammingDistance(x, y))