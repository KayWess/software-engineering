import abc


class Actuator(metaclass=abc.ABCMeta):

    def __init__(self, name, room):
        self.name = name
        self.room = room