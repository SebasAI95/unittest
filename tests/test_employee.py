import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        self.per_1 = Employee('sebas', 'quintero', 5000)
        self.per_2 = Employee('jhony', 'quintero', 6000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test email')
        self.assertEqual(self.per_1.email, 'sebas.quintero@email.com')
        self.assertEqual(self.per_2.email, 'jhony.quintero@email.com')

        #  change the person's names
        self.per_1.name = 'norberto'
        self.per_2.name = 'aracelly'

        self.assertEqual(self.per_1.email, 'norberto.quintero@email.com')
        self.assertEqual(self.per_2.email, 'aracelly.quintero@email.com')


    def test_fullname(self):
        print('test fullname')
        self.assertEqual(self.per_1.fullname, 'sebas quintero')
        self.assertEqual(self.per_2.fullname, 'jhony quintero')


    def test_pay_raise(self):
        print('test apply raise')
        self.assertEqual(self.per_1.apply_raise, '5500.0')
        self.assertEqual(self.per_2.apply_raise, '6600.0')


    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.per_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/quintero/May')
            self.assertEqual(schedule, 'Success')

if __name__ == "__main__":
    unittest.main()

