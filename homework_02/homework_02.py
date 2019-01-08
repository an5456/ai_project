def peakIndexInMountainArray(A):
    """
    :type A: List[int]
    :rtype: int
    """
    # return A.index(max(A))
    for i in range(len(A)-1):
        if A[i+1] < A[i]:
            a_max = A[i]
            return A.index(a_max)


print(peakIndexInMountainArray([9, 1, 15, 3]))  # 预期输出 1def peakIndexInMountainArray(A):
