class Person:
    def __init__(self
                name = '',
                nationality = '',
                birth = '',
                address = ''):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("eito:", self.name)
        print("nihonn:", self.name)
        print("2004:", self.birth)
        print("nihon:", self.address)
