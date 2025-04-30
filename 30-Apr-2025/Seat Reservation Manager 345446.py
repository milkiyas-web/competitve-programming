# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.seat = [i for i in range(1, n+1)]

    def reserve(self) -> int:
        if self.seat:
            x = heapq.heappop(self.seat)
            # print(self.seat)
            return x
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seat, seatNumber)

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)