import socket
import random


IP = "192.168.0.157"
PORT = 8003
MAX_OPEN_REQUESTS = 5



def process_client(clientsocket, numero):
    print(clientsocket)
    numeros_ip = clientsocket.recv(2048).decode("utf-8")
    sorteo = (int(numeros_ip[0])+int(numeros_ip[1])+int(numeros_ip[2])+int(numeros_ip[3]))%10
    if sorteo == numero:
        mensaje = "Enhorabuena, has ganado"
        salida = str.encode(mensaje)
        clientsocket.send(salida)
    else:
        mensaje = "Lo siento, ha perdido"
        salida = str.encode(mensaje)
        clientsocket.send(salida)

    clientsocket.close()







serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        numero = random.randint(0,9)
        # accept connections from outside
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket, numero)


except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)