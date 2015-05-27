import unittest
from interface import *

class TestCase(unittest.TestCase):
    def test_empty(self):
        class FooInterface(interface):
            pass

        @implements(FooInterface)
        class FooImplementation(object):
            pass

        foo = FooImplementation()

    def test_complex(self):
        class FooInterface(interface):
            def foo(self, a, b=7, *args, **kwargs):
                pass

        @implements(FooInterface)
        class FooImplementation(object):
            def foo(self, a, b=7, *args, **kwargs):
                pass

        foo = FooImplementation()

    def test_missing_method(self):
        class FooInterface(interface):
            def foo(self):
                pass

        with self.assertRaises(NotImplementedError):
            @implements(FooInterface)
            class FooImplementation(object):
                pass

    def test_missing_argument(self):
        class FooInterface(interface):
            def foo(self, arg):
                pass

        with self.assertRaises(NotImplementedError):
            @implements(FooInterface)
            class FooImplementation(object):
                def foo(self):
                    pass

    def test_renamed_argument(self):
        class FooInterface(interface):
            def foo(self, arg):
                pass

        with self.assertRaises(NotImplementedError):
            @implements(FooInterface)
            class FooImplementation(object):
                def foo(self, arrrrg):
                    pass

    def test_extra_argument(self):
        class FooInterface(interface):
            def foo(self, arg):
                pass

        with self.assertRaises(NotImplementedError):
            @implements(FooInterface)
            class FooImplementation(object):
                def foo(self, arg, ument):
                    pass

    def test_different_defaults(self):
        class FooInterface(interface):
            def foo(self, arg=7):
                pass

        with self.assertRaises(NotImplementedError):
            @implements(FooInterface)
            class FooImplementation(object):
                def foo(self, arg=8):
                    pass

    def test_different_order(self):
        class FooInterface(interface):
            def foo(self, a, b):
                pass

        with self.assertRaises(NotImplementedError):
            @implements(FooInterface)
            class FooImplementation(object):
                def foo(self, b, a):
                    pass

    def test_missing_kwargs(self):
        class FooInterface(interface):
            def foo(self, **kwargs):
                pass

        with self.assertRaises(NotImplementedError):
            @implements(FooInterface)
            class FooImplementation(object):
                def foo(self):
                    pass

if __name__ == '__main__':
    unittest.main()