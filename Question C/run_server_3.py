from servers.server import Server

if __name__ == "__main__":
    
    server_3 = Server((1,1), 1236, "server_3", [])
    
    server_3.bind_socket_to_port()

    server_3.run_server()
