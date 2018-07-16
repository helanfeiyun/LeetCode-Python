# author Helanfeiyun
#
# def generate(numRows):
#     num = [[1],[1,1]]
#     if numRows <=2:
#         return num[:numRows]
#     row = []
#     for i in range(2,numRows):
#         for j in range(i-1):
#             row.append(sum(num[-1][j:j+2]))
#         num.append([1] + row + [1])
#         row = []
#     return num



def generate(numRows):
    if numRows == 0:
        return []
    res = [[1]]
    for i in range(1, numRows):
        res += [list(map(lambda x,y: x+y, [0]+res[-1],res[-1]+[0]))]
    return res

print(generate(1))
# def generate(self, numRows):
#     """
#     :type numRows: int
#     :rtype: List[List[int]]
#     """
#     res = [[1]]
#
#     for i in range(1, numRows):
#         res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
#
#     return (res[:numRows])