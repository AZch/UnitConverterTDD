class Converter():
    def __init__(self):
        self.__names = []

    def addQuantities(self, name, arrFromQuant):
        self.__names.append(name)

    def getNames(self):
        return self.__names

    def getQuantities(self):
        return [[1]]