class Person:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
    def info(self):
        print(self.name,self.phone,self.email)
