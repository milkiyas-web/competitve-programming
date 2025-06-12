# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = sum(x.isalpha() for x in s)
        s= s.lower()
        res = []
        for m in range(1<<n):
            x = list(s)
            lett_idx = 0
            for i in range(len(x)):
                if x[i].isalpha():
                    if (m >> lett_idx) & 1:
                        x[i] = x[i].upper()
                    lett_idx+=1
            res.append("".join(x))
        return res
            
        