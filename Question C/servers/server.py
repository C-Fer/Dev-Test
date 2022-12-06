import socket
import datetime
import time
import random
import sys

class Server:

  def __init__(self, location, port, name, distance_to_clients):
    
    self.name = name
    self.port = port
    self.location = location
    self.distance_to_clients = distance_to_clients
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
  
  def bind_socket_to_port(self):

    self.socket.bind((socket.gethostname(), self.port))
    self.socket.listen(3)


  def run_server(self):

   while True:
   
    clientsocket, address = self.socket.accept()

    print(f"Connection from {address} has been established.")

    while True: 
      
        current_hour = str(datetime.datetime.now().strftime("%H:%M:%S")) + f" from server {self.name}"

        clientsocket.send(bytes(current_hour,"utf-8"))

        russian_roulette = random.randint(0, 12)

        print(russian_roulette)

        if russian_roulette == 1:
          print("Killing socket")
          sys.exit()

        time.sleep(5)
