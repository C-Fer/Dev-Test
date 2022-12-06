import socket
from collections import deque
import time

class Client:

  def __init__(self, location, name, server_ports):
    
    self.name = name
    self.location = location
    self.server_ports = server_ports
    self.socket_list = []
    self.cache = deque([], maxlen=6)


  def creating_socket_list(self):

    for server_port in self.server_ports:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((socket.gethostname(), server_port))
      self.socket_list.append(s)
    
  
  def build_data_cache(self):

    while True:
      
      while True:

        try: 
          msg_1 = self.socket_list[0].recv(50)

          msg_2 = self.socket_list[1].recv(50)

          decoded_msg_1 = msg_1.decode("utf-8")

          decoded_msg_2 = msg_2.decode("utf-8")

          self.cache.appendleft(decoded_msg_1)

          self.cache.appendleft(decoded_msg_2)

          if decoded_msg_1 == "":
            del(self.socket_list[0])
            print(self.socket_list)
            break

          if decoded_msg_2 == "":
            del(self.socket_list[1])
            print(self.socket_list)
            break

        except:
          break  
  
        print(self.cache)
        print(f"Size of cache: {len(self.cache)}")