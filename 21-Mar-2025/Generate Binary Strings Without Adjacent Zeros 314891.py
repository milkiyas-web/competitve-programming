# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        arr = []
        def rec(n, s):
            # if n == 1:
            #     arr.append("0")
            #     arr.append("1")
            # if len(s) == n:
            #     arr.append("".join(s))
            #     # return 
            # if s:
            #     if s[-1] == "0":
            #         rec(n, s.append("1"))
            #         print(s)
            #     else:
            #         rec(n, s.append("0"))
            #         rec(n, s.append("1"))
            # else:
            #     print(s)
            #     s.append("0")
            #     print(s)
            if len(s) == n:
                arr.append("".join(s))
                return 
            for i in ("0", "1"):
                if s:
                    if s[-1] == "0" and i == "0":
                        continue
                s.append(i)
                rec(n, s)
                s.pop()

        rec(n, [])
        return arr
            
        