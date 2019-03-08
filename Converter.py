class Converter():
    def __init__(self):
        self.__names = []
        self.__quantitiesMult = []

    def addQuantities(self, name, arrFromQuant):
        self.__quantitiesMult.append(arrFromQuant)
        self.__names.append(name)

    def getNames(self):
        return self.__names

    def getQuantities(self):
        return self.__quantitiesMult