import socket   
import threading
import json
import ipaddress
from python_service.loan.loan import calculate_car_loans


# the constants we are expecting in the JSON object sent by the client
JSON_HASH_METHOD = "method-name"
JSON_HASH_ARGS = "args"
METHOD_NAME = "calculate_car_loans"
METHOD_ARG_1_NAME = "principle_amount"
METHOD_ARG_2_NAME = "interest_rate"

# thread function that will take care of the connected client

def handle_connected_client(conn):
    while True:
        # receive data from the client
        data = conn.recv(1024)
      
        # variable to store the return message back to the client
        returnData = ""

        if not data:
            # no data has been received, the client has closed the conection
            print("Client has closed the connection. Shutting down service")
            break
        elif data.decode() == "test":
            returnData = calculate_car_loans(10000, 10)
        else:

            JsonResult = ""
            InvalidJsonError = ""
            json_object = {}
            JsonObject_Valid = True
            try:
                # the client has sent a message, check what it is
                json_object= json.loads(data.decode())               
            except:
                InvalidJsonError = "Error: Invalid JSON Data"
                JsonObject_Valid = False
            
            if JsonObject_Valid:
                successful_conversion, JsonResult = check_json_object(json_object) 

                if successful_conversion:
                
                    principle = float(JsonResult[METHOD_ARG_1_NAME])
                    interest = float(JsonResult[METHOD_ARG_2_NAME])

                    if principle <= 0:
                        returnData = "Error: Principle Amount must be greater than 0"
                    elif interest < 0:
                        returnData = "Error: Interest amount cannot be less than 0"
                    else:
                        returnData = calculate_car_loans(principle, interest)
                else:
                    returnData = JsonResult
            else:
                 returnData = InvalidJsonError 

            
           


        # convert the return data into a proper JSON object
        string_to_return = json.dumps(returnData)

        # send the return values back to the client
        conn.sendall(string_to_return.encode())


    #we are finished with this client connection, close it
    conn.close()


    
# Check if the JSON object sent by the client is a proper request for the service
def check_json_object(Json_object):

    print(Json_object)
    args = {}
    # check that we can properly get a dictionary out of the JSON object
    try:
        methodName = Json_object[JSON_HASH_METHOD]
    except:
        return (False, "Error: JSON object improperly formatted: Could not access the method-name of the JSON object received")

    # check that the method name matches the name of the method of the service
    if methodName != METHOD_NAME:
        return (False, f"Error: Method name received did not match a method this service provides. Must be named: {METHOD_NAME}")

    # check that we can access the method arguments
    try:
        args = Json_object[JSON_HASH_ARGS]
    except:
        return (False, f"Error:Method arguments could not be found. Make sure you have a dictionary of arguments called {JSON_HASH_ARGS}at the top level of your json object")

    #check that the arguments dictionary contains the proper arguments 
    try: 
        _ = float(args[METHOD_ARG_1_NAME])
    except:
         return (False, f"Error: Make sure {METHOD_ARG_1_NAME} is present in the argument list as a valid float")

    try: 
        _ = float(args[METHOD_ARG_2_NAME])
    except:
         return (False, f"Error: Make sure {METHOD_ARG_2_NAME} is present in the argument list as a valid float")

    # if we reached this point, return True with the argument list
    return (True, args)

