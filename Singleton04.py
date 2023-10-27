"""Singleton es un patrón de diseño creacional que le permite garantizar
que una clase tenga solo una instancia, al tiempo que proporciona
un punto de acceso global a esta instancia."""


class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.getinstance())

    @classmethod
    def getinstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()  # class initialized, but object not created
print("Object created", Singleton.getinstance())  # Object gets created here
s1 = Singleton()  # instance already created

