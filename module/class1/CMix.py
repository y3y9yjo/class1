class CPerson:
    objectCount = 0
    def __init__(self,id,name,department,Email,birthday) -> None:
        self.__id = id
        self.__name = name
        self.__department = department
        self.__Email = Email
        self.__birthday = birthday
        CPerson.ObjectCountAdd()
    
    @staticmethod
    def ObjectCountAdd():
        CPerson.objectCount += 1
    
    @staticmethod
    def getObjectCount():
        return CPerson.objectCount
    @property
    def id(self):
        return "None"
    @property
    def name(self):
        return "None"
    @property
    def Department(self):
        return "None"
    @property
    def Email(self):
        return "None"
    @property
    def birthday(self):
        return "None"
    @id.getter
    def getID(self):
        return self.__id
    @id.setter
    def setID(self,newID):
        self.__id = newID
    @name.getter
    def getName(self):
        return self.__name
    @name.setter
    def setName(self,newName):
        self.__name = newName
    @Department.getter
    def getDepartment(self):
        return self.__department
    @Department.setter
    def setDepartment(self,newDpartment):
        self.__department = newDpartment
    @Email.getter
    def getEmail(self):
        return self.__Email
    @Email.setter
    def setEmail(self,newEmail):
        self.__Email = newEmail
    @birthday.getter
    def getBirthday(self):
        return self.__birthday
    @birthday.setter
    def setBirthday(self,newBirthday):
        self.__birthday = newBirthday


class Cstudent(CPerson):
    def __init__(self, id, name, department, Email, birthday) -> None:
        super().__init__(id, name, department, Email, birthday)


class Cteacher(CPerson):
    def __init__(self, id, name, department, Email, birthday) -> None:
        super().__init__(id, name, department, Email, birthday)


class Cstaff(CPerson):
    def __init__(self, id, name, department, Email, birthday) -> None:
        super().__init__(id, name, department, Email, birthday)
