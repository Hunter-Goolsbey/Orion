from .commissionRules import commissionRules
#from employeeStatbook import employeeStatbook

class employee:
    def __init__(self):
        self.__employeeID = "10304050"
        self.__commissionAmount = 0
        self.__employeeName = ""

        
    def setEmployeeName(self, employeeName :str):
        self.__employeeName = employeeName

    def getEmployeeName(self) -> str:
        return self.__employeeName
    
    def changeEmployeeID(self, newEmployeeID :str):
        self.__employeeID = newEmployeeID

    def getEmployeeID(self) -> str:
        return self.__employeeID
    
    def setCommissionRules(self, commissionRules :commissionRules):
        self.__commissionRules = commissionRules
    
    def getCommissionRules(self) -> commissionRules:
        return self.__commissionRules
    
    def setCommissionAmount(self, commissionAmount: float):
        self.__commissionAmount = commissionAmount

    def getCommissionAmount(self) -> float:
        return self.__commissionAmount