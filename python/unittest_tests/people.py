
class Person:
    """Makes people"""

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def email(self):
        return f"{(self.name).lower()}.{(self.surname).lower()}@email.com"

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"