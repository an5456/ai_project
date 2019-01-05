def numJewelsInStones(J, S):
  count = 0
  for i in S:
      if i in J:
          count+=1
  print(count)


numJewelsInStones("aA","aAAbbbb")  # 预期输出 3