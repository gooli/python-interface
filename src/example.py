from interface import interface, implements

class comestible(interface):
    def eat(self): pass
    def buy_from(self, supermarket): pass
    def mix_with(self, *ingredients): pass
    def cook_with(self, **ingredients): pass
    def cook(self, temperature=100): pass

@implements(comestible)
class hamburger(object):
    
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

print hamburger()