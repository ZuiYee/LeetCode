# class Solution:
#     def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
#         lis = []
#         for querie in queries:
#             B = A
#             sum = 0
#             B[querie[1]] = querie[0] + A[querie[1]]
#             for num in B:
#                 if num %2 == 0:
#                     sum += num
#             lis.append(sum)
#         return lis


class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        S = 0
        for x in A:
            if x % 2 == 0:
                S += x
        lis = []
        for i, j in queries:
            if A[j] % 2 == 0:
                S -= A[j]
            A[j] += i
            if A[j] % 2 ==0:
                S += A[j]
            lis.append(S)
        return lis


