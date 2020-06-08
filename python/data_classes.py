from dataclasses import dataclass

@dataclass
class Person:
    """Class used to create people"""
    name: str
    age: int
    height: float
    gender: str = "Male"

    def get_email(self) -> str:
        return f"{(self.name).lower()}@email.com"

a = Person("Muzi", 32, 1.75)
print(a.name)
print(a.get_email())