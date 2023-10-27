import sqlite3

"""un servicio en la nube que implica múltiples operaciones de lectura y escritura en la base de datos. 
Lo que necesitamos unir aquí es la base de datos porque la aplicación web llamará a una API que eventualmente
 operará en la base de datos. Usaremos sqlite3, viene incluido con Python."""


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db.sqlite3')
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()
print(f"db1={db1}\ndb2={db2}")
