class Person:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
    def __delete__(self, instance):
        print("deleted")
human=Person("qwerty",123432,"dg@gf.rdf")
# admin01 branch da merge admin01
# conflict merge
