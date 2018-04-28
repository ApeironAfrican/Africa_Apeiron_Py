import Cars_Class

class Car_Specialists:

    def __init__(self,name,car_type,skill,amount):
        self.name = name
        self.car_type = car_type
        self.skill = skill
        self.amount = amount

    def persona_details(self):
        return '{} is a {} for the vehicle {} and earns {} annually'.format(self.name,self.skill,self.car_type,self.amount)
    
class mechanic(Car_Specialists):
    pass

driver = Car_Specialists('Carl Max', 'Volvo', 'driver', '$50,000')
mech = mechanic('Dickson Martin', 'Volvo', 'mechanic', '$150,000')

print(driver.persona_details())
print(mech.persona_details())
#print(help(mech))
list = [102, 343 , 'que', 2.2, 50]
print(list[0:4])
