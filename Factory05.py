from abc import ABCMeta, abstractstaticmethod


class Persona(metaclass=ABCMeta):
    @abstractstaticmethod
    def mostrar_person():
        """Interface Method"""


class Docente(Persona):
    def __init__(self):
        self.name = "Nombre Docente"

    def mostrar_person(self):
        print("Yo soy un docente")


class Estudiante(Persona):
    def __init__(self):
        self.name = "Nombre Estudiante"

    def mostrar_person(self):
        print("Yo soy un estudiante")


class PersonFactory:
    @staticmethod
    def crear_persona(tipo_person):
        if tipo_person == "Estudiante":
            return Estudiante()
        if tipo_person == "Docente":
            return Docente()
        print("Tipo Inválido")
        return -1


if __name__ == '__main__':
    opt = input("Selecccione el tipo de persona que desea crear\n")
    person= PersonFactory.crear_persona(opt)
    person.mostrar_person()
