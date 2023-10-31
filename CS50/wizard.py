class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing name')
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, house, name):
        super().__init__(name)
        self.name = name
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, subject, name):
        super().__init__(name)
        self.name = name
        self.subject = subject

    ...


wizard = Wizard('Albus')
student = Student('Harry', 'Gryffindor')
professor = Professor('Severus', 'Defense Against the Dark Arts')
