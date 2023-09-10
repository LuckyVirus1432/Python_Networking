import sys
import socket

def create_socket():
    try:
        global host
        global port
        global s
    
        host =""
        port = 9999
        s = socket.socket()
    
    except socket.error as msg:
        print("Connection error :- ", str(msg))
    
    
def bind_socket():
    try:
        global host
        global port
        global s
    
        print("Binding to the port ", port)
        s.bind((host, port))
        s.listen(10)
   
    except socket.error as msg:
        print("Binding error :- ", msg, "\nRetrying...")
        bind_socket()
        
def socket_accept():
     conn, addr = s.accept()
     print(f"Connection has been established with IP = {addr[0]} PORT = {str(addr[1])}")
     send_commands(conn)
     conn.close()
     

def send_commands(conn):
     while True:
         cmd = input()
         if cmd == 'q' or cmd == 'quit' or cmd == 'exit':
             conn.close()
             s.close()
             sys.exit()
         if len(str.encode(cmd)) > 0:
             conn.send(str.encode(cmd))
             client_response = str(conn.recv(1024), "utf-8")
             print(client_response, end="")

     
 
def main() :
    create_socket()
    bind_socket()
    socket_accept()
    
main()




                     
                                          
                                                               
                                                                                    
                                                                                                                       
        
     
     
     
        
        
        
        