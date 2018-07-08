# author Helanfeiyun

A = [0]
def plusOne( A):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    for j in range(len(A)-1,-1,-1):
        if A[j] !=9:
            A[j] += 1
            return A
        else:
            A[j] = 0
    if A[0] == 0:
        A.insert(0,1)
        return A
print(plusOne(A))

