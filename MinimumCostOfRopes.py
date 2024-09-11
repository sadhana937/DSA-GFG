import heapq
from typing import List

class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: List[int]) -> int:
    
        # code here
        heapq.heapify(arr)
        total_cost = 0
        while len(arr) > 1:
            num1 = heapq.heappop(arr)
            num2 = heapq.heappop(arr)
            total_cost += num1 + num2
            heapq.heappush(arr, num1 + num2)
        
            
        return total_cost
