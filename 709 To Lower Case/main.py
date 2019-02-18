class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        str_list = []
        for char in str:
            if 65 <= ord(char) <= 90:
                print(char)
                str_list.append(chr(ord(char)+32))
            elif 97 <= ord(char) <= 122:
                str_list.append(char)
            else:
                raise Exception
        print(str_list)
        return "".join(str_list)


if __name__ == '__main__':
    s = Solution()
    print(s.toLowerCase('LOVddDdY'))