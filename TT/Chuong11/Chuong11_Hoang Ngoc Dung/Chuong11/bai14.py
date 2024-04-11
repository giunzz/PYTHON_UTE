def checkphone(d):
    for i in d:
        if i['phone'][-1] == '8':
            print(i['name'])
def check_email(d):
    for i in d:
        if i['email'] == '':
            print(i['name'])

if __name__ == '__main__':
    d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
    print("All the users whose phone number ends in an 8:")
    checkphone(d)
    print("All the users that don’t have an email address listed: ")
    check_email(d)