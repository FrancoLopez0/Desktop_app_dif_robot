from interfaces import IRobot, IMobileRobot


def RHermes(IRobot, IMobileRobot):
    def __init__(self):
        self.id = None
        self.port = None
        self.speed = None
        self.direction = None

    def setPos(self, x, y):
        pass

    def setAngle(self, angle):
        pass

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setPort(self, port):
        self.port = port

    def getPort(self):
        return self.port

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def setDirection(self, direction):
        self.direction = direction

    def getDirection(self):
        return self.direction
