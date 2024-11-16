users = {
    "oleg": "oleglox", 
    "root": "rootrott89", 
    "jdjfdh54": "hrhfjjhfh",
    "erevan": "erevan2345",
}



def login(username, password):
    if username in users:
        if users[username] == password:
            return True
        else: 
            return False
    else:
        return False

print(login("oleg", "2342342"))
