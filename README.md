# Python Car Laon Microservice

### About
A Python Car Loan Microservice that takes in the principle amount of your car loan, as well as the interest rate.
It returns the monthly payments required to pay off the laon for 36 months, 48 months and 60 months.
Uses the Python socket library to accept and respond to incoming requests

Originally part of a larger microservice project, this application can be ran on it's own.


### Setup
The service runs on localhost, and runs on port 12345. Simply download the zip file, go into the python_service directory, and run 'python -m python_service'

### Calling the service
The service parses incoming requests for the following JSON data:

{
  "method": "calculateCarLoan",
    "args": {
        "principleAmount" : "10000",
        "interestRate": "4"
    }
}

method: The name of the function to be called. In this case, if it's anything other than 'calculateCarLoan', it returns an error
args: The arguments of the function 
 - principleAmount: The principle loan amount
 - interestRate: The percent interest rate of the loan



### Responses

The microservice returns the following upon a **successful** request:

{
  "error": false, 
  "response": 
    { 
      "names": ["payment36Month", "payment48Month", "payment60Month"],
      "values": ["295.24", "225.79", "184.17"]
    }
}

error : A boolean stating whether an error occured. Will be false upon a successfull request
response: The return values of the method
  - name: An array of strings, containing the names of the returned values
  - values: The corrosponding values of the above returned values.



The microservice returns the following when it receives a **Bad** request:

{
  "error": true,
  "response": {
                "message": "principleAmount is not present in the argument list as a valid float"
              }
 }


error : A boolean stating whether an error occured. Will be true upon a bad request
response: The rresponse of the microservice
  - message: a string containing details of the bad request
