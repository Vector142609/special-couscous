class Pen(object):
    def __init__(self , name , color , type , ink_size , company):
        self.name = name
        self.color = color
        self.company = company
        self.ink_size = ink_size
        self.type = type


a = Pen("Name : Robomax," , "Colour : Blue," , "Company : Rorito" , "Refill size : 150," , "Type : Gel,")
print(a.name , a.color, a.company, a.ink_size, a.type)
        