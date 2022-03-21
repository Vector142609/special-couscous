class Car(object):
    def __init__(self , model , color , company , speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

    def acc(self):
        print("Accelerating")

    def cgear(self):
        print("Gear Changed")

a = Car("Model : Bolide," , "Colour : Red and Black," , "Company : Buggati," , "Top speed : 400,")
print(a.model , a.color, a.company, a.speed_limit)
        
        