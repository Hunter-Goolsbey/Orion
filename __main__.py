#import sys
from employee import employee
from team import team
from rules import rules
from commissionRules import commissionRules
from organization import organization
from revenue import revenue

#merge test :: Development -> main

organization = organization()

organization.setOrganizationName("The Spokesman Review")
print(organization.getOrganizationName())


team1 = team()
team2 = team()

team1.setTeamName("Team 1")
team2.setTeamName("Team 2")

print(team1.getTeamName())
print(team2.getTeamName())


Jennifer = employee()
Bob = employee()
Leroy = employee()

Jennifer.setEmployeeName("Jennifer")
Bob.setEmployeeName("Bob")
Leroy.setEmployeeName("Leroy")


team1.addEmployee(Jennifer)
team1.addEmployee(Bob)
team2.addEmployee(Leroy)

for employee in team1.getEmployees():
    print(employee.getEmployeeName())

print(len(team1.getEmployees()))
print(len(team2.getEmployees()))


print("Employee Name is: ", Jennifer.getEmployeeName())
print("Employee Name is: ", Bob.getEmployeeName())

Jennifer.changeEmployeeID("0008")
Bob.changeEmployeeID("10303050")

print(Jennifer.getEmployeeID())
print(Bob.getEmployeeID())

employeeCommissionRules1 = commissionRules()
rulebook1 = rules()
rulebook2 = rules()

rulebook1.setRule("MonthlyBonus", 100.00)
rulebook1.setRule("QuarterlyBonus", 50.00)
rulebook2.setRule("Annual Bonus", 80.00)

print(rulebook1.getRule())
employeeCommissionRules1.add(rulebook1)
employeeCommissionRules1.add(rulebook2)
Jennifer.setCommissionRules(employeeCommissionRules1.getCommissionRules())
Bob.setCommissionRules(employeeCommissionRules1.getCommissionRules())

for i in Jennifer.getCommissionRules():
    print(i.getRule())
print(Bob.getCommissionRules())

#Bob.changeEmployeeID("10304050")
#print(Bob.getCommissionRules())

revenue1 = revenue()
print(revenue1.sumMonthRangeByTerritory(2,2, "0008"))
print(revenue1.sumByTerritory("0008"))

