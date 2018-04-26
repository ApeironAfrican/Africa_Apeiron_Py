#Class functions

class cars:
    def __init__(self,name,speed,year,price):
        self.name = name
        self.speed = speed
        self.year = year
        self.price = price

    def car_features(self):        
        return 'The car of choice is {} with speed of {} for the year {} total cost amounting to {}'.format(self.name,self.speed,self.year,self.price)

