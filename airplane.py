class Airplane:
    
    def __init__(self, airplanType, airplanRange, seats):
        
        self.airplanType = airplanType
        self.airplanRange = airplanRange
        self.seats = seats

    def setPlane(self, airplanType):
        
        if self.airplanRange >= self.distance:
            return True
        else:
            return False
        

