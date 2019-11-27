from datetime import datetime
import logging
from python_service.customLogging.loggingConstants import *






def customlog(message, messageType, level = 2, fields = None):

    logMessage = ""

    if messageType == MESSAGE_TYPE_INFO:
        logMessage = ""
    elif messageType == MESSAGE_TYPE_ERROR:
        logMessage = ""
    elif messageType == MESSAGE_TYPE_RECEIVED_REQUEST:
      logMessage = ""
    elif messageType == MESSAGE_TYPE_CLIENT_CONNECTED:
        logMessage = ""
    elif messageType == MESSAGE_TYPE_SHUTTING_DOWN_SERVICE:
        logMessage = ""
    elif messageType == MESSAGE_TYPE_BAD_INPUT:
        logMessage = ""

    logMessage += message
    # check if there were any fields we should parse through
    if fields != None:
        logMessage += "      | "
        logMessage += " {"
         # handle the fields passed in
        for key in fields.keys():
            logMessage += "[" + str(key) + " = " + str(fields[key]) + "]"

        logMessage += " }"
   
        

    if level == LOGLEVEL_DEBUG:
        logging.debug(logMessage)
    elif level ==  LOGLEVEL_INFO:
        logging.info(logMessage)
    elif level ==  LOGLEVEL_WARNING:
        logging.warning(logMessage)
    elif level == LOGLEVEL_ERROR:
        logging.error(logMessage)
    elif level == LOGLEVEL_CRITICAL:
        logging.critical(logMessage)
    else:
        logging.info(logMessage)
    
    print(message)

