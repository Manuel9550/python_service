import socket   


from python_service.loan.loan import calculate_car_loans
from python_service.connection_handling.connection_handling import handle_connected_client

def runClient(ip, port):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        handle_connected_client(s)  

