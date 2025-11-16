from abc import abstractmethod
from abc import ABCMeta


class IRobot(metaclass=ABCMeta):
    @abstractmethod
    def setId(self):
        pass

    @abstractmethod
    def getId(self):
        pass

    @abstractmethod
    def setPort(self):
        pass

    @abstractmethod
    def getPort(self):
        pass
