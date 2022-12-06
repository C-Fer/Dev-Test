from servers.server import Server

if __name__ == "__main__":
    
    server_2 = Server((1,1), 1235, "server_2", [])
    
    server_2.bind_socket_to_port()

    server_2.run_server()
