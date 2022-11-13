class UndergroundSystem:
    def __init__(self):
        self.travels = {}
        self.transit = {} #depicts customers currently still in transit

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.transit[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        entryStat, t_entry = self.transit.pop(id)
        edge = (entryStat, stationName)
        if edge in self.travels:
            avg, n = self.travels[edge]
            self.travels[edge] = ((avg * n + (t - t_entry)) / (n + 1), n + 1)
        else:
            self.travels[edge] = (t - t_entry, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.travels[(startStation, endStation)][0]