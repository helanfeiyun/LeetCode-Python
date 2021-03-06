# author Helanfeiyun




# def getRow(rowIndex):
#     """
#     :type rowIndex: int
#     :rtype: List[int]
#     """
#     if rowIndex < 0:
#         return []
#     if rowIndex == 0:
#         return [1]
#     num = [1, 1]
#     row = []
#     for i in range(2, rowIndex + 1):
#         for j in range(i - 1):
#             row.append(sum(num[j:j + 2]))
#         num = [1] + row + [1]
#         row = []
#     return num
#
# print(getRow(5))

def getRow(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0] + row, row + [0])]
    return row
