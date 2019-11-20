ERROR_ZERO_MONTHS = "Number of Months must be greater than 0"


def calculate_car_loan_by_month(principal_amount, interest_rate, number_of_months):
    rate = interest_rate / 1200
    monthly_payments = 0


    # if the interest amount is 0, then use a modified version of the equation so that we don't get a divide by 0 error
    if interest_rate == 0:
        monthly_payments = round(principal_amount / number_of_months ,2)
    else:
        monthly_payments = round(((rate + (rate / ( ((1 + rate)**number_of_months) -1))) * principal_amount),2)
    
    return monthly_payments

def calcualte_car_loans(principal_amount, interest_rate):

    # make sure the value received is rounded to the nearest two decimal places
    principal_amount_rounded = round(principal_amount, 2)

    month_result_36 = calculate_car_loan_by_month(principal_amount_rounded,interest_rate, 36)
    month_result_48 = calculate_car_loan_by_month(principal_amount_rounded,interest_rate, 48)
    month_result_60 = calculate_car_loan_by_month(principal_amount_rounded,interest_rate, 60)

    return [month_result_36, month_result_48, month_result_60]

    