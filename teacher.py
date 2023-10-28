import copy
from prototype03 import Person


class Teacher(Person):

    def __init__(self, name: str, course: str):
        super().__init__(name)
        self._course = course

    def clone(self):
        return copy.copy(self)

    def display(self):
        # return super().display()
        print("El profesor fue clonado:")
        print("------------------------")
        print(f"Nombre: {self._name}")
        print(f"Cual profesor: {self._course}")

    def get_course(self):
        return self._course

    def set_course(self, course: str):
        self._course = course
