import socket   
import threading
from python_service.loan.loan import calculate_car_loans
from python_service.connection_handling.connection_handling import handle_connected_client


import signal
import sys
def signal_handler(sig, frame):
        print('Sigint Detected. Closing down main thread')
        sys.exit(0)


def run():

   signal.signal(signal.SIGINT, signal_handler)
    
   #create the socket object we are going to be using to listen for connections
   s = socket.socket()        

  
   # set timeout 2 second
   s.settimeout(2)

   # reserve a port on your computer in our 
   # case it is 12345 but it can be anything 
   port = 12345              
    
   # Next bind to the port 
   # we have not typed any ip in the ip field 
   # instead we have inputted an empty string 
   # this makes the server listen to requests  
   # coming from other computers on the network 
   s.bind(('', port))         
   print("socket binded to %s" %(port))
   
   # put the socket into listening mode. Putting in a queue of ten, in case we get lots of messages at once
   s.listen(10)      
   print("socket is listening")            
   
      

   # a forever loop until we interrupt it or  
   # an error occurs 

   keep_open_connection = True

   while keep_open_connection: 
    
      try:
         # Establish connection with client. 
         conn, addr = s.accept()      
         print('Got connection from', addr)
         #start_new_thread(handle_connected_client,(conn))
         keep_open_connection = handle_connected_client(conn)
      except KeyboardInterrupt:
         print('Keyboard Interrupt detected. Closing down main thread')
         break
      except TimeoutError:
         keep_open_connection = True
      except socket.timeout:
          keep_open_connection = True
   
       

   # close the socket

   s.close()
