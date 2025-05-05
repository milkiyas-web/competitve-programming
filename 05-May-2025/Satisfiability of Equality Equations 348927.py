# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # n = len(equations)
        n = 200
        parent = [i for i in range(n)]
        rank = [0] * (n)
        visited = set()
        # for i in range(len(equations)):
        #     for j in range(4):
        diff = []
                
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            # if b == "=":
            x_ = find(x)
            y_ = find(y) 
            if x_ != y_:
                # return False
                if rank[x_] > rank[y_]:
                    parent[y_] = x_
                elif rank[x_] < rank[y_]:
                    parent[x_] = y_
                else:
                    parent[y_] = x_
                    rank[x_] += 1

        
        for a,b,c,d in equations:
            print(b)
            if b == "=":
                union(ord(a)-97, ord(d)-97)
            else:
                diff.append((ord(a)-97, ord(d)-97))
        print(diff)
        print(parent)
        for a, b in diff:
            # print(find(a),find(b)
            if find(a) == find(b):
                return False
        return True