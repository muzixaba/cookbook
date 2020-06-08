import unittest
from people import Person

class TestPerson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass runs at the very begining")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass runs at the very end")

    def setUp(self):
        print("setUp method runs at begining of each test")
        self.person_1 = Person("Muzi", "Xaba", 32)
        self.person_2 = Person("Nkanyezi", "Xaba", 3)

    def tearDown(self):
        print("tearDown method at the end of each test")

    def test_full_name(self):
        print("test full_name")
        self.assertEqual(self.person_1.full_name, "Muzi Xaba")
        self.assertEqual(self.person_2.full_name, "Nkanyezi Xaba")

    def test_email(self):
        print("test email")
        self.assertEqual(self.person_1.email, "muzi.xaba@email.com")
        self.assertEqual(self.person_2.email, "nkanyezi.xaba@email.com")

# mocking???????

if __name__ == "__main__":
    unittest.main()