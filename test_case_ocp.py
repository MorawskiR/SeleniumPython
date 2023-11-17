import unittest


#podejscie obiektowe
#OCP - open case principle
#SOLID  klasa ktora mozna rozszerzac
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(True,False) #add assertion here


if __name__ == '__main__':
    unittest.main()