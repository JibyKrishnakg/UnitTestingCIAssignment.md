import re
print("This is the Final.py file")
print("Python thinks this is called {}".format(__name__))


def is_email(email):
    x = r'^[a-zA-Z0-9]+[\._]?[\-_]?[\__]?[a-zA-Z0-9]+[" "__]?[@][" "__]?[a-zA-Z0-9]+[\-]?[a-zA-Z0-9]+[.][a-zA-Z]{2}'
    print(x)
    print(email)
    if re.match(x, email):
        print("Format matched")
    else:
        print("Format not matched")


def is_email_space(emailtestsp): 
    if re.search(" ", emailtestsp):
        print("Space detected")
        email_stensprm(emailtestsp)
    else:
        print("No Space")
        is_email(emailtestsp)


def email_stensprm(staend):
    if staend.startswith(" ") or staend.endswith(" "):
        print("Space in starting or end detected")
        space_removar(staend)
    else:
        is_email(staend)


def space_removar(emailspr):
    emailspr = emailspr.replace(" ","")
    print(emailspr)
    is_email(emailspr)


if __name__ == '__main__':
    emailtest = " rohit00.-gupta00 @mc-Bnsolutions.aiiA" 
    print(emailtest)
    is_email_space(emailtest)