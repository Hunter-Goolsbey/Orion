from .employee import employee
class team:
    def __init__(self):
        self.__assignedEmployees = []
        self.__teamName = ""
        self.__teamLeadName = ""


    def setTeamName(self, teamName :str):
        self.__teamName = teamName

    def getTeamName(self) -> str:
        return self.__teamName

    def addEmployee(self, employee :employee):
        self.__assignedEmployees.append(employee)

    def getEmployees(self) -> list:
        return self.__assignedEmployees
    
    def setTeamLead(self, teamLeadName :str):
        self.__teamLeadName = teamLeadName

    def getTeamLead(self) -> str:
        return self.__teamLeadName
    