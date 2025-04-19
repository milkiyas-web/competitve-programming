# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        def dfs(room):
            visited[room] = True
            for r in rooms[room]:
                if not visited[r]:  
                    dfs(r)
        dfs(0)
        print(visited)
        return all(visited)

        