from account import *

class Test:
    def setup_method(self):
        self.p1 = account('John', 12)
        self.p2 = account('Sam', 77)

    def teardown(self):
        del self.p1
        del self.p2

    def test_init(self):
        




    def test_deposit(self):
        assert self.p1.