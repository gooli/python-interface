from interface import interface, implements

class Comestible(interface):
    def __init__(self, hungry): pass
    def eat(self): pass
    def buy_from(self, supermarket): pass
    def mix_with(self, *ingredients): pass
    def cook_with(self, **ingredients): pass
    def cook(self, temperature=100): pass

@implements(Comestible)
class Hamburger(object):
    def __init__(self, hungry): 
        pass
    
    def eat(self):
        pass

    def buy_from(self, supermarket):
        pass
    
    def mix_with(self, *ingredients):
        pass
    
    def cook_with(self, **ingredients):
        pass
    
    def cook(self, temperature=100):
        pass
