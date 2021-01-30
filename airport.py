class Airport(object):

    d1 = {'Toronto' :"YYZ",
        'Ottawa' :"YOW",
        'Frankfurt' :"FRA",
        'Vancouver' :"YVR",
        'HongKong' : "HKG"}

    d2 = {'Toronto' :"CAN",
        'Ottawa' :"CAN",
        'Frankfurt' :"GER",
        'Vancouver' :"CAN",
        'HongKong' : "HKG"}
    
    def __init__(self, code, country):
        self.code = code
        self.country = country


