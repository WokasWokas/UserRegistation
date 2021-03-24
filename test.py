import os
os.system("cls")

class Data:
    users = []

class User(object):
    def __init__(self, user: dict):
        self.name = user.get("name")
        self.exp = user.get("exp")
        self.lvl = user.get("lvl")
        self.maxExp = user.get("maxExp")
        self.password = user.get("password")
    
    def info(self):
        print(f"-Information about {self.name}")
        print(f"-Level: {self.lvl}")
        print(f"-Expierence: {self.exp} / {self.maxExp}")

    def add_exp(self, exp: int):
        add_exp(user=self, exp=exp)
        add_lvl(user=self)

    def exit_user(self):
        result = exit_user(user=self)
        if result == False:
            return result
        else:
            print("-User can't exit")

    def delete_user(self):
        delete_user(user=self)
        result = exit_user(user=self)
        if result == False:
            return result
        else:
            print("-User can't exit")

def format_user(**kwargs):
    return {"name": kwargs.get("name"), "exp": kwargs.get("exp"), "lvl": kwargs.get("lvl"),
        "maxExp": kwargs.get("maxExp"), "password": kwargs.get("password")}

def add_exp(user: User, exp: int):
    try:
        user.exp += exp
        return 0
    except:
        return 1

def add_lvl(user: User):
    try:
        while True:
            if user.lvl == 10 or user.lvl == "max":
                user.lvl = "max"
                user.exp = user.maxExp
                user.maxExp = "Infinity"
                return 0
            if user.exp >= user.maxExp:
                user.lvl += 1
                user.maxExp *= 2
            else:
                user.exp = 0
                return 0
    except:
        return 1

def create_user(name: str, password: str):
    try:
        user = format_user(name=name, lvl=0, exp=0, maxExp=10, password=password)
        Data.users.append(user)
        return User(user)
    except:
        return 1
    
def connect_user(name: str, password: str):
    try:
        for user in Data.users:
            if user["name"] == name:
                if user["password"] == password:
                    return User(user)
        print("[Warn] User not found")
        return False
    except:
        return False
            
def exit_user(user: User):
    try:
        del(user)
        return False
    except:
        print("[Error] User not deleted")
        return 1
        

def delete_user(user: User):
    try:
        for userList in Data.users:
            if userList["name"] == user.name:
                Data.users.remove(userList)
                return 0
        print("-User not found")
        return 1   
    except:
        return 1

def save_user(user):
    if type(user) == User:
        for name in Data.users:
            if name.get("name") == user.name:
                user = format_user(name=user.name, exp=user.exp, lvl=user.lvl,
                        maxExp=user.maxExp, password=user.password)
                Data.users[Data.users.index(name)] = user

def check_menu(user):
    if user == False:
        return start_menu()

def start_menu():
    commands = ["help", "create_user", "connect_user"]
    while True:
        option = input("start_menu:")
        if option == commands[0]:
            for command in commands:
                print(f"-{command}")
        if option == commands[1]:
            name = input("Name:")
            password = input("Password:")
            user = create_user(name=name, password=password)
            return user
        if option == commands[2]:
            name = input("Name:")
            password = input("Password:")
            user = connect_user(name=name, password=password)
            return user
    
def user_menu(user: User):
    commands = ["help", "info", "exit_user", "add_exp","delete_user", "exit"]
    while True:
        option = input(f"{user.name}:")
        if option == commands[0]:
            for command in commands:
                print(f"-{command}")
        if option == commands[1]:
            user.info()
        if option == commands[2]:
            return user.exit_user()
        if option == commands[3]:
            exp = input("Exp:")
            try:
                user.add_exp(int(exp))
            except ValueError:
                print("-Wrong value")
        if option == commands[4]:
            return user.exit_user()
        if option == commands[5]:
            print("Program closing")
            exit()


user = False
while True:
    try:
        user = check_menu(user)
        if user != False:
            user = user_menu(user)
        save_user(user)
    except KeyboardInterrupt:
        save_user(user)
        exit("\n-User close program")