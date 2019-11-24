import socket   
import threading
from python_service.loan.loan import calculate_car_loans
from python_service.connection_handling.connection_handling import handle_connected_client


def run():
    
    #create the socket object we are going to be using to listen for connections
    s = socket.socket()        

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
    while True: 
    
       # Establish connection with client. 
       conn, addr = s.accept()      
       print('Got connection from', addr)
       #start_new_thread(handle_connected_client,(conn))
       x = threading.Thread(target=handle_connected_client, args=(conn,))
       x.start()
       

    # close the socket

    s.close()
