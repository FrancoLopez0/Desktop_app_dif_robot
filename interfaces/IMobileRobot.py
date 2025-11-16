from abc import abstractmethod
from abc import ABCMeta


class IMobileRobot(metaclass=ABCMeta):
    @abstractmethod
    def setSpeed(self):
        pass

    @abstractmethod
    def getSpeed(self):
        pass

    @abstractmethod
    def setDirection(self):
        pass

    @abstractmethod
    def getDirection(self):
        pass
