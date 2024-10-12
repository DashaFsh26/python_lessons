real_password = "1234"
real_username = "oleg"
def login(password, username):
    if password == real_password or real_username == username:
        return True
    else:
        return False
        
print(login("1234","oleg"))