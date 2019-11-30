import unittest
from python_service.loan.loan import calculate_car_loan_by_month
from python_service.loan.loan import calculate_car_loans
from python_service.loan.loan import ERROR_ZERO_MONTHS
from python_service.connection_handling.connection_handling import JSON_HASH_METHOD

from python_service.connection_handling.connection_handling import check_json_object

class ValidationTest(unittest.TestCase):

    def test_calculates_correct_amount(self):
        self.assertEqual(1100.65, calculate_car_loan_by_month(150000,8,360))
    
    def test_handles_0_interest_correctly(self):
        self.assertEqual(1000, calculate_car_loan_by_month(10000,0,10))

    def test_handles_0_principle_amount_correctly(self):
        self.assertEqual(0, calculate_car_loan_by_month(0,12,10))

    def test_handles_0_months_correctly(self):
        self.assertEqual(ERROR_ZERO_MONTHS, calculate_car_loan_by_month(30000,60,0))

class InputTest(unittest.TestCase):


    def test_float_input(self):
        input = {"method": "calculateCarLoan", "args": { "principleAmount" : '103680', "interestRate": '0'} }
        result = {"principleAmount" : '103680', "interestRate" : '0'}


        self.assertEqual((True, result), check_json_object(input))


if __name__ == '__main__':
    unittest.main()
