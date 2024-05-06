import re
class BasePasswordManager:

    def old_passwords(self):
        old_password = ['012345', '2134siph', '2134sip$']
        self.old_password = old_password[-1]
        return self.old_password
    
    def get_password(self):
        current_password = self.old_password
        self.current_password = current_password
        return "Current password is " + self.current_password
        

    def is_correct(self, password=input('please type in your password: ')):
        self.password = password
        print("New passsword is the same as the current password:",self.password == self.current_password)
        return self.password

class PasswordManager(BasePasswordManager):

   
    def set_password(self):
        if len(self.password) <8:
            print("New Password must have 8 characters or More")
            print("Password Change : UNSUCCESSFUL")
        elif self.password == self.current_password:
            print("Password Change: No Changes Detected")
        else:
            print("Password Change:SUCCEDDFUL")
            print()

current = PasswordManager()
current.old_passwords()
current.get_password()
current.is_correct()
current.set_password()
