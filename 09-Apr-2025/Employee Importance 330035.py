# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emplo = {emp.id: emp for emp in employees}
        def dfs(empid):
            employees = emplo[empid]
            total = employees.importance
            for sub_id in employees.subordinates:
                total+=dfs(sub_id)
            return total
            # print(employees.subordinates)
            # print(emplo[empid].importa)
        return dfs(id)



        
        
