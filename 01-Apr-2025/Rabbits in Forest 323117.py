# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        r = defaultdict(int)
        min_count = 0 

        for i in answers:
            r[i]+=1

        for x,y in zip(r.keys(),r.values()) :
                min_count = min_count +ceil(y/(x+1))*(x+1)
        
        return min_count
    