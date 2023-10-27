# coding=utf-8
class SoyUnico(object):
    class __SoyUnico:
        def __init__(self):
            self.nombre = None

        def __str__(self):
            return 'MyClass(Nombre=' + str(self.nombre)
            # return self + ' ' + self.nombre

    instance = None

    def __new__(cls):
        if not SoyUnico.instance:
            SoyUnico.instance = SoyUnico.__SoyUnico()
        return SoyUnico.instance

    def __getattr__(self, nombre):
        return getattr(self.instance, nombre)

    def __setattr__(self, nombre, valor):
        return setattr(self.instance, nombre, valor)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"


if __name__ == '__main__':
    person = SoyUnico()
    person.nombre = "Huberth Fallas"
    print(person)
    print(person.__repr__())
    person2 = SoyUnico()
    person2.nombre = "Huberth Fallas Romero"
    print(person)
    print(person2.__repr__())
