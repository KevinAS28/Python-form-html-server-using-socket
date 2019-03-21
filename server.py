import socket
from threading import Thread
import sys
ip = "0.0.0.0"
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((ip, port))
sock.listen()
checkpoint = 0
print("listening...")
finish = False

def client_handler(client_socket, info):
 with open("form.html", "rb") as baca:
  baca = baca.read()
 global checkpoint
 if finish:
  sys.exit(0)
 print("Connection from %s:%d" %(info[0], info[1]))
 print(client_socket.recv(1024))
 client_socket.send(baca)
 print("okay{x}".format(x=checkpoint))
 client_socket.close()
 checkpoint+=1

while True:
 try:
  client, addr = sock.accept()
  Thread(target=client_handler, args=(client, addr)).start()
 except KeyboardInterrupt as e:
  print("Stop\r\n")
  sock.close()
  sys.exit(0)
  
 
