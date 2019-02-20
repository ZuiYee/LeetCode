class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        odd = 1
        even = 0
        ans = copy.deepcopy(A)
        for a in A:
            if a % 2 == 0:
                ans[even] = a
                even += 2
            else:
                ans[odd] = a
                odd += 2

        return ans


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            A = stringToIntegerList(line);

            ret = Solution().sortArrayByParityII(A)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()