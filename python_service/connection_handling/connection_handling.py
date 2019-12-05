import socket   
import threading
import json
import ipaddress
from python_service.loan.loan import calculate_car_loans

import signal
import sys

import errno

from python_service.customLogging.loggingConstants import LOGLEVEL_INFO, LOGLEVEL_ERROR
from python_service.customLogging.customLogging import customlog

# the constants we are expecting in the JSON object sent by the client
JSON_HASH_METHOD = "method"
JSON_HASH_ARGS = "args"
METHOD_NAME = "calculateCarLoan"
METHOD_ARG_1_NAME = "principleAmount"
METHOD_ARG_2_NAME = "interestRate"




# thread function that will take care of the connected client

def handle_connected_client(conn):
    connection_open = True
    Successfull_Connection_End = True
    while connection_open:
        # variable to store the return message back to the client
        returnData = ""
        data = None
       
        error = False

        # receive data from the client
        try:
            data = conn.recv(1024)
        except (KeyboardInterrupt, SystemExit):
            connection_open = False
            Successfull_Connection_End = False
            error = True
            customlog("Keyboard Interrupt detected", LOGLEVEL_INFO)
            returnData = "SIGINT detected on the server side, closing the connection"

        
      
        

        if connection_open:
            if not data:
                # no data has been received, the client has closed the conection
                print("Client has closed the connection.")
                break
            elif data.decode() == "test":
                returnData = calculate_car_loans(10000, 10)
                error = False
            else:

                JsonResult = ""
                InvalidJsonError = ""
                json_object = {}
                JsonObject_Valid = True
                try:
                    # the client has sent a message, check what it is
                    json_object= json.loads(data.decode())          
                    customlog("Received Request from client", LOGLEVEL_INFO, {"Input Received":data.decode()})  
                except:
                    InvalidJsonError = "Parsing messgage error on the service side"
                    customlog("Bad JSON Input", LOGLEVEL_ERROR, {"Input Received":data.decode()})
                    JsonObject_Valid = False
                    error = True

                if JsonObject_Valid:
                    successful_conversion, JsonResult = check_json_object(json_object) 

                    if successful_conversion:
                    
                        principle = float(JsonResult[METHOD_ARG_1_NAME])
                        interest = float(JsonResult[METHOD_ARG_2_NAME])

                        if principle <= 0:
                            returnData = "Principle Amount must be greater than 0"
                            customlog(returnData, LOGLEVEL_ERROR, {"Input Received":json.dumps(json_object)})
                            error = True
                        elif interest < 0:
                            returnData = "Interest amount cannot be less than 0"
                            customlog(returnData, LOGLEVEL_ERROR, {"Input Received":json.dumps(json_object)})
                            error = True
                        else:
                            try:
                                returnData = calculate_car_loans(principle, interest)
                                error = False
                            except:
                                error = true
                                returnData = "Result was too large"
                    else:
                        returnData = JsonResult
                        error = True
                else:
                     returnData = InvalidJsonError
                     error = True 
        
       # prepare the json message to send back to the requester
        results = {
            "error": error,
            "response" : {}
        }

        if error:
            results["error"] = True
            results["response"]["message"] = returnData
        else:
            results["response"] = returnData

        # convert the return data into a proper JSON object
        print("Sending: ", json.dumps(results))
        

        # send the return values back to the client
        customlog("Sending Result to client", LOGLEVEL_INFO, results) 
        conn.sendall(json.dumps(results).encode())

  

    return Successfull_Connection_End

    
# Check if the JSON object sent by the client is a proper request for the service
def check_json_object(Json_object):

    args = {}
    # check that we can properly get a dictionary out of the JSON object
    try:
        methodName = Json_object[JSON_HASH_METHOD]
    except:
        message = "JSON object improperly formatted: Could not access the method-name of the JSON object received"
        customlog(message, LOGLEVEL_ERROR, {"Input Received":json.dumps(Json_object)})
        return (False, message)

    # check that the method name matches the name of the method of the service
    if methodName != METHOD_NAME:
        message = f"Method name received did not match a method this service provides. Must be named: {METHOD_NAME}"
        customlog(message, LOGLEVEL_ERROR, {"Input Received":json.dumps(Json_object)})
        return (False, message)

    # check that we can access the method arguments
    try:
        args = Json_object[JSON_HASH_ARGS]
    except:
        message = "Problem on the service side parsing arguments."
        logMessage = f"Method arguments could not be found. Make sure you have a dictionary of arguments called {JSON_HASH_ARGS}at the top level of your json object"
        customlog(logMessage,LOGLEVEL_ERROR, {"Input Received":json.dumps(Json_object)})
        return (False, message)

    #check that the arguments dictionary contains the proper arguments 
    try: 
        _ = float(args[METHOD_ARG_1_NAME])
    except:
        message = f"{METHOD_ARG_1_NAME} is not present in the argument list as a valid float"
        customlog(message, LOGLEVEL_ERROR, {"Input Received":json.dumps(Json_object)})
        return (False, message)

    try: 
        _ = float(args[METHOD_ARG_2_NAME])
    except:
        message = f"{METHOD_ARG_2_NAME} is not present in the argument list as a valid float"
        customlog(message, LOGLEVEL_ERROR, {"Input Received":json.dumps(Json_object)})
        return (False, message)

    # if we reached this point, return True with the argument list
    return (True, args)

