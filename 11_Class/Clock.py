import winsound

class Clock():
    id = None
    price = None
    
    def __init__(self,id,price):
        self.id = id
        self.price = price

    
    def ring(self):
        winsound.Beep(2000,3000)
