import re

email = ["fjladfk_iasdfad234@sdlkjf23335.in","ha@git@int.cz","prashant24_@gmail.com"]

def is_valid(email):
    regex = "^[a-zA-Z0-9\-\_]+@[A-Za-z0-9]+[\.][a-zA-Z]{1,3}$"
    if(re.search(regex, email)):
        return True
    else:
        return False


def filter_mail(emails):
    return list(filter(is_valid, emails))

print(filter_mail(email))