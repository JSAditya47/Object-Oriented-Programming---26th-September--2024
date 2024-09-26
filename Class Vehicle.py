class Vehicle:
    
    def __init__(self, max_speed, mileage):
        
        self.max_speed = max_speed
        self.mileage = mileage
        
tesla = Vehicle(120, 11)
lambo = Vehicle(280, 20)

print("Tesla's Max Speed: ", tesla.max_speed)
print("Tesla's Mileage: ", tesla.mileage)

print("Lambo's Max Speed: ", lambo.max_speed)
print("Lambo's Mileage: ", lambo.mileage)

if lambo.max_speed > tesla.max_speed:
    print("Lambo is Faster than Tesla!!")
    
else:
    print("Still lambo is better than Tesla because It is a Petrol Based Car")