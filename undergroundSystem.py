class UndergroundSystem:
    """
    Purpose: Designs an underground system that keeps track of customer travel
    times between different stations.
    """
    def __init__(self):
        self.customers = {}
        self.timeCalculation = {}


    def checkIn(self, id: int, stationName: str, t: int):
        self.customers[id] = [stationName, t]

        if stationName not in self.timeCalculation:
            self.timeCalculation[stationName] = [[t]]
        else:
            self.timeCalculation[stationName].append([t])


    def checkOut(self, id: int, stationName: str, t: int):
        popped = self.customers.pop(id)
        startStation = popped[0]
        startTime = popped[1]
        self.timeCalculation[startStation].append([stationName, t - startTime])


    def getAverageTime(self, startStation: str, endStation: str):
        start = self.timeCalculation[startStation]
        mysum = count = 0
        for x in start:
            if type(x) is int: pass
            else:
                if x[0] == endStation:
                    mysum += x[1]
                    count += 1
        if count != 0:        
            return mysum / count
        else: return

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)