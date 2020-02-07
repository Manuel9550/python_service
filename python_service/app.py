import socket   
import threading
from python_service.loan.loan import calculate_car_loans
from python_service.connection_handling.connection_handling import handle_connected_client
import logging
from python_service.customLogging.loggingConstants import LOGLEVEL_INFO
from python_service.customLogging.customLogging import customlog


import signal
import sys
def signal_handler(sig, frame):
        customlog('Sigint Detected. Closing down main thread', 3)
        sys.exit(0)


def run():



   logging.basicConfig(filename='python_service\\logfile.log',level=logging.DEBUG,format='%(levelname).4s:[%(asctime)s.%(msecs)03d]: %(message)s  ',datefmt='%Y-%m-%dT%H:%M:%S')
   logging.info("Started the application")
   signal.signal(signal.SIGINT, signal_handler)
    
   #create the socket object we are going to be using to listen for connections
   s = socket.socket()        

  
   # set timeout 2 second
   s.settimeout(2)


   port = 12345              
    

   s.bind(('', port))         
   customlog("socket binded", LOGLEVEL_INFO, {"Ip Address":"127.0.0.1","port":port})
   
   # put the socket into listening mode. Putting in a queue of ten, in case we get lots of messages at once
   s.listen(10)      
   customlog("socket is listening", LOGLEVEL_INFO, {"Ip Address":"127.0.0.1","port":port})         
   
      

   keep_open_connection = True

   while keep_open_connection: 
    
      try:
         # Establish connection with client. 
         conn, addr = s.accept()      
         customlog("Received Connection", LOGLEVEL_INFO, {"Address Received From":addr})  
   
         keep_open_connection = handle_connected_client(conn)
      except KeyboardInterrupt:
         customlog("Keyboard Interrupt detected", LOGLEVEL_INFO)
         break
      except TimeoutError:
         keep_open_connection = True
      except socket.timeout:
          keep_open_connection = True
   
       

   # close the socket

   s.close()
