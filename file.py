class Person:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def __delete__(self, instance):
        print("deleted")
    def info(self):
        print("name :",self.name,"phone :",self.phone)
human=Person("Ali",123443)
human.info()
# master branch da git merge master01
# fast-forward merge