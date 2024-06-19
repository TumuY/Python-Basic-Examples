class server():
    def __init__(self,name):
        self.name = name

    @classmethod
    def login(cls,name,pw):
        for item in user.userlist:
            if name == item.kulNick and pw == item.kulPas:
                return print("Welcome.")
            else:
                return print("Error.")

class user():
    userlist = []

    def __init__(self,userNick,userPw):
        self.kulNick = userNick
        self.kulPas = userPw
        user.Add(self)

    @classmethod
    def Add(cls,userN):
        user.userlist.append(userN)
