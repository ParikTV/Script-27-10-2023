from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def display(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name
