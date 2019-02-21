import re
class Solution:
    def myAtoi(self, str: 'str') -> 'int':
        str = str.strip()
        try:
            res = re.search('(^.*?-?[\+\~]?\d+)', str).group()

            res = int(res)
            res = res if res <= 2147483647 else 2147483647
            res = res if res >= -2147483648 else -2147483648
        except:
            res = 0

        return res