class Student():
    def __init__(self,name,surname,schoolnumber,grade):
        self.name = name
        self.surname = surname
        self.schoolnumber = schoolnumber
        self.setgrade(grade)

    def setgrade(self,arg):
        if 8< arg<13:
            self.__grade = arg
        else:
            self.__grade = -1

    def getgrade(self):
        return self.__grade

    def getInfo(self):
        if self.__grade == -1:
            print("Grade must be between 9 to 12.")
        return print("{},{},{},{}".format(self.name,self.surname,self.schoolnumber,self.__grade))
