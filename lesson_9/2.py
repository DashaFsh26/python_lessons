users = {"oleg": "oleglox", "root": "rootrott89", "jdjfdh54": "hrhfjjhfh"}


def login(username, password):
    if username in users:
        if users[username] == password:
            return False
    else:
        return False

print(login("oleg", "oleglox"))
print(login("sdfsdfsdfdfs", "sdfsfs"))