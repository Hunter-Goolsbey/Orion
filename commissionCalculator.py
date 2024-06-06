from employee import employee
from revenue import revenue
from goals import goals

class commissionCalculator:
    def __init__(self, employee, revenue, goals):
        self.__revenue = revenue
        self.__goals = goals
        self.__employee = employee