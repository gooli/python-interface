# python-interface

Implementation of interface contracts in Python.
A simple alternative to Zope Interfaces (https://github.com/zopefoundation/zope.interface).

Originally by @pmatiello, reworked by @gooli.

# Usage

To define an interface simply derive from the `interface` class. It's actually an empty class, but it's nice to document our interfaces this way.

To mark a class as implementing an interface, use the `@implements` decorator on the class.

Interface complience is checked during class creation and you usually only need to import the module to make sure the classes implement everything correctly.

In the following code, the `Hamburger` class is incorrectly defining the `cook` method (the default value for temperature is missing) and an exception is thrown during import.

    from interface import interface, implements
    
    class Comestible(interface):
      def eat(self): pass
      def buy_from(self, supermarket): pass
      def mix_with(self, *ingredients): pass
      def cook_with(self, **ingredients): pass
      def cook(self, temperature=100): pass
    
    @implements(Comestible)
    class Hamburger(object):
      
      def eat(self):
        pass
    
      def buy_from(self, supermarket):
        pass
        
      def mix_with(self, *ingredients):
        pass
      
      def cook_with(self, **ingredients):
        pass
      
      def cook(self):
        pass

This is what the exception looks like:

    NotImplementedError: Class 'Hamburger' must implement method 'cook(self, temperature=100)' 
    defined in interface 'Comestible'.

# Todo

- Create and deploy a PyPI package
- Add support for Python 3 type annotations
