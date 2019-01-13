def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    print([s in J for s in S])
    return sum([s in J for s in S])

print(numJewelsInStones("aA","aAAbbbb") ) # 预期输出 3
print(sum([True, True, True]))