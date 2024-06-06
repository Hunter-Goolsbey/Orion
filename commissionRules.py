from .rules import rules
class commissionRules:
    def __init__(self):#, employeeID):
        #self.__employeeID = employeeID
        self.__commissionRules = []


    def getCommissionRules(self) -> list:
        """Returns list of commission rules"""
        return self.__commissionRules
        

    def add(self, rules :rules):
        """Append rulebook to commission rules list"""
        self.__commissionRules.append(rules)