import unittest2
from employee import Employee


class TestEmployee(unittest2.TestCase):

    def test_email(self):
        per_1 = Employee('sebas', 'quintero', 5000)
        per_2 = Employee('jhony', 'quintero', 6000)
        self.assertEqual(per_1.email, 'sebas.quintero@email.com')
        self.assertEqual(per_2.email, 'jhony.quintero@email.com')

        #  change the person's names
        per_1.name = 'norberto'
        per_2.name = 'aracelly'

        self.assertEqual(per_1.email, 'norberto.quintero@email.com')
        self.assertEqual(per_2.email, 'aracelly.quintero@email.com')


    def test_fullname(self):
        per_1 = Employee('sebas', 'quintero', 5000)
        per_2 = Employee('jhony', 'quintero', 6000)
        self.assertEqual(per_1.fullname, 'sebas quintero')
        self.assertEqual(per_2.fullname, 'jhony quintero')


    def test_pay_raise(self):
        per_1 = Employee('sebas', 'quintero', 5000)
        per_2 = Employee('jhony', 'quintero', 6000)
        self.assertEqual(per_1.apply_raise, 5500.0)
        self.assertEqual(per_2.apply_raise, 6600.0)


if __name__ == "__main__":
    unittest2.main()

