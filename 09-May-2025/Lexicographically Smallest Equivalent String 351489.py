# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(1000)]
        def find(x):
            while x!= parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            if r1!=r2:
                if r1 < r2:
                    parent[r2] = parent[r1]
                else:
                    parent[r1] = parent[r2]
            
        for i in range(len(s1)):
            union(ord(s1[i])-97, ord(s2[i])-97)
        ans = ""
        for s in baseStr:
            x = find(ord(s)-97)
            ans+=chr(x+97)
        return ans.lower()


        