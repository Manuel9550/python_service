import sys
from python_service.app import run
from python_service.client import runClient

if __name__ == '__main__':
    if  len(sys.argv) == 3 :

        # check that a valid ip and port were given
        port = 0
        ip = sys.argv[1]
        port = 0
      
        try:
            if (1 <= int(sys.argv[2]) and int(sys.argv[2]) <= 65535):
                runClient(ip, int(sys.argv[2]))
            else:
                raise ValueError
        except ValueError:
            print(f"{sys.argv[2]} is NOT a VALID port number.")   
    else:
        run()