import socket

hote= "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))

print("Connection of {}".format(port))

socket.send(b"Hey I have received your request baby")

print("Close")
socket.close()
