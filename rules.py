class rules:
    def __init__(self):
        self.__rulebook = {}

    def setRule(self, rule :str, value :float):
        """Create new rule, included in the rulebook.  Identical rule names will overwrite previous values"""
        self.__rulebook[rule] = value

    def getRule(self) -> dict:
        """Returns complete rulebook"""
        return self.__rulebook