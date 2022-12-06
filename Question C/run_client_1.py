from clients.client import Client

if __name__ == "__main__":
    
    client_1 = Client((1,1), "client_1", [1234,1235,1236])
    
    client_1.creating_socket_list()
    
    client_1.build_data_cache()