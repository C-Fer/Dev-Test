from servers.server import Server

if __name__ == "__main__":
    
    server_1 = Server((1,1), 1234, "server_1", [])
    
    server_1.bind_socket_to_port()

    server_1.run_server()
