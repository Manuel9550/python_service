ERROR_ZERO_MONTHS = "Number of Months must be greater than 0"


def calculate_car_loan_by_month(principal_amount, interest_rate, number_of_months):
    rate = interest_rate / 1200
    final_result = 0


    # if the interest amount is 0, then use a modified version of the equation so that we don't get a divide by 0 error
    if number_of_months == 0:
        final_result = ERROR_ZERO_MONTHS
    elif interest_rate == 0:
        final_result = round(principal_amount / number_of_months ,2)
    else:
        final_result = round(((rate + (rate / ( ((1 + rate)**number_of_months) -1))) * principal_amount),2)
    
    return final_result

def calculate_car_loans(principal_amount, interest_rate):

    # make sure the value received is rounded to the nearest two decimal places
    principal_amount_rounded = round(principal_amount, 2)

    month_result_36 = calculate_car_loan_by_month(principal_amount_rounded,interest_rate, 36)
    month_result_48 = calculate_car_loan_by_month(principal_amount_rounded,interest_rate, 48)
    month_result_60 = calculate_car_loan_by_month(principal_amount_rounded,interest_rate, 60)

    returnDict = {}
    returnDict["payment36Month"] = str(month_result_36)
    returnDict["payment48Month"] = str(month_result_48)
    returnDict["payment60Month"] = str(month_result_60)

    return returnDict

    