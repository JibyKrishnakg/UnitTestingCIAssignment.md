import re
print("This is the Final.py file")
print("Python thinks this is called {}".format(__name__))


def is_email_space(emailtestsp): 
    if re.search(" ", emailtestsp):
        print("Space detected")
        email_stensprm(emailtestsp)
    else:
        print("No Space")
        is_email(emailtestsp)


if __name__ == '__main__':
    emailtest = " rohit00.-gupta00 @mc-Bnsolutions.aiiA" 
    print(emailtest)
    is_email_space(emailtest)