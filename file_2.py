class Person:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def __delete__(self, instance):
        print("deleted")
    def info(self):
        print("name :",self.name,"phone :",self.phone)
human=Person("Vali",2345645)
# main branch da git merge --squash main01
# git commit -m "Change"
# squash merge method bo'ladi
