import socket

IP = "192.168.0.157"
PORT = 8003

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))


except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

IP = IP.replace(".", "")
IP = IP[-4:]
numeros_ip = str.encode(IP)
s.send(numeros_ip)
resultado = s.recv(2048).decode("utf-8")
print(resultado)



s.close()
