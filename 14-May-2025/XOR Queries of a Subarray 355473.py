# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        ans = []
        for i in range(1, len(arr)):
            prefix[i] = prefix[i-1] ^ arr[i]
        for a,b in queries:
            if a == 0:
                ans.append(prefix[b])
            else:
                ans.append(prefix[b] ^ prefix[a-1])
        return ans




        

