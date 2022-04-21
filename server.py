import socket

SIZE = 1024
FORMAT = "utf-8"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 3000))
fileRecieved = s.recv(SIZE).decode(FORMAT)
print("File recieved succesfully")
print("Content of the file recieved:")
print(fileRecieved)