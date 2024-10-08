from typing import List
import math

class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    answer = right
    while left <= right:
      k = (left+right)//2
      i, j, hours = 0, len(piles) - 1, 0
      while i <= j:
        if i != j:
          hours += math.ceil( piles[i] / k ) + math.ceil( piles[j] / k )
        else:
          hours += math.ceil( piles[i] / k )
        i += 1
        j -= 1
      if hours <= h:
        answer = min(answer, k)
        right = k - 1
      else:
        left = k + 1
    return answer

if __name__ == "__main__":
  s = Solution()
  s1 = s.minEatingSpeed([3,6,7,11], h = 8)
  s2 = s.minEatingSpeed([30,11,23,4,20], h = 5)
  s3 = s.minEatingSpeed([30,11,23,4,20], h = 6)

  print("paso" if s1 == 4 else "fallo")
  print("paso" if s2 == 30 else "fallo")
  print("paso" if s3 == 23 else "fallo")
