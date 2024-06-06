class organization:
    def __init__(self):
        self.__organizationID = "001"
        self.__organizationName = ""
        self.__employees = []
        #self.__organizationName = "Spokesman Review"

    def setOrganizationID(self, organizationID :str):
        """Sets organization ID.  ID IS MANUALLY GENERATED AND SHOULD NOT BE CHANGED LIGHTLY"""
        self.__organizationID = organizationID

    def getOrganizationID(self) -> str:
        """Returns organization ID"""
        return self.__organizationID
    
    def setOrganizationName(self, organizationName :str):
        """Sets organization name"""
        #f = open("DB.txt", "w")
        #f.write(organizationName)
        #f.close()
        self.__organizationName = organizationName

    def getOrganizationName(self) -> str:
        """Returns organization name"""
        #f = open("DB.txt", "r")
        return self.__organizationName
    
    def addEmployee(self, employee):
        self.__employees.append(employee)

    def getEmployees(self) -> list:
        """Returns list of employees belonging to organization"""
        return self.__employees

    

    