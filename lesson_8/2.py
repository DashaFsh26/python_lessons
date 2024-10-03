real_password = "some_password"

def login(password):
    
    if real_password == password:
        return True
    else:
        return False

# python3 -i lessson_8/2.py