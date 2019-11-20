import unittest
from python_service.loan.loan import calculate_car_loan_by_month
from python_service.loan.loan import calcualte_car_loans

class ValidationTest(unittest.TestCase):

    def test_calcualtes_correct_amount(self):
        self.assertEqual(1100.65, calculate_car_loan_by_month(150000,8,360))
    
    def test_handles_0_interest_correctly(self):
        self.assertEqual(1000, calculate_car_loan_by_month(10000,0,10))

    def test_handles_0_principle_amount_correctly(self):
        self.assertEqual(0, calculate_car_loan_by_month(0,12,10))

if __name__ == '__main__':
    unittest.main()
