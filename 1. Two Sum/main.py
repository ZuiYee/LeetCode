class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        dict = {}
        indexList = []
        for (index, value) in enumerate(nums):
            _value = target - value
            if _value not in dict:
                dict[value] = index
            else:
                _index = dict[_value]
                indexList.extend([_index, index])
        return indexList