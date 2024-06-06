class revenue:
    def __init__(self):
        self.__data = [[1, "SR.com","0008", 1200.00], [2, "SR.com", "0008", 320.00], [2, "SR.com", "0008", 2300.00]]
        #query 12 months of historical revenue from informer
        #query 12 months of goal ammounts


    def sumMonthRangeByTerritory(self, startMonth :int, endMonth :int, territoryID :str) -> float:
        """Return total revenue for given territory and period month range"""
        self.__sumRange = 0
        for row in self.__data:
            if row[0] >= startMonth and row[0] <= endMonth:
                self.__sumRange += row[-1]
        return self.__sumRange

    def sumByTerritory(self, territoryID :str) -> float:
        """Return total revenue for given territory over the last 12 months, ending in current month"""

        self.__sumAll = 0

        for row in self.__data:
            if territoryID == row[2]:
                self.__sumAll += row[-1]
        return self.__sumAll
            
        #pass revenue ammounts to commission calculator
        #commission calculator pushes final commissions to employees
        pass