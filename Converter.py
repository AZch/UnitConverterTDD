class Converter():
    def __init__(self):
        self.__names = []
        self.__quantitiesMult = []

    def addQuantities(self, name, arrFromQuant):
        if len(self.__quantitiesMult) == 0:
            self.__quantitiesMult.append([1])
        else:
            self.__quantitiesMult.append(arrFromQuant)
        self.__names.append(name)

    def getNames(self):
        return self.__names

    def getQuantities(self):
        return self.__quantitiesMult