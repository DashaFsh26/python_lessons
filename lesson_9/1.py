real_emails = {"fhfhh@sdfsdf.ru", "sto@sto.ru", "goog@ssdf.ru"}

def check_email(email):
    if email in real_emails:
        return True
    else:
        return False

def add_email(email):
    real_emails.add(email)


print(real_emails)

add_email("new_email@n.ru")
add_email("new_email@n.ru")

print(real_emails)

list_ = [1, 2, 3, 4, 4]
set_ = {1, 2, 3, 4, 4}
print(set_)