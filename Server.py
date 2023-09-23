import socket
import subprocess

# Define the IP address and port to listen on
HOST = 'localhost'
PORT = 2728

# Function to handle incoming client requests
def handle_client(client_socket):
    # Receive data from the client
    request = client_socket.recv(4096).decode('utf-8')
    #print("request: ", request,"\n")
    # Extract the requested file name from the request
    request_type = request.split(' ')[0]
    requested_file = request.split(' ')[1]
    #print(requested_file, request_type )

    # Default to serving 'index.php' if no specific file is requested
    if requested_file == '/':
        requested_file = '/index.php'
        # php_output = subprocess.check_output(["./php/php.exe","./htdocs/index.php"], stderr=subprocess.STDOUT, cwd="./")
        # response = f"""HTTP/1.1 200 OK\nContent-Type: text/html\n\n{php_output.decode('utf-8')}"""
        # client_socket.send(response.encode('utf-8'))
    
    
        

    # Define the document root directory
    document_root = './htdocs'

    # Construct the full file path
    if request_type == "GET" or request_type == "get":
        file_path = document_root + requested_file.split('?')[0]
    else:
        file_path = document_root + requested_file

    print(file_path)
    
    # Check if the requested file exists
    if ".html" in file_path:
        print("HTML file detected")
        file=open(file_path, 'r')
        msg = " ".join([i for i in file])
        response = f"""HTTP/1.1 200 OK\nContent-Type: text/html\n\n{msg}"""
        client_socket.send(response.encode('utf-8'))    

    elif "favicon.ico" in file_path:
        print("favicon file detected")
        response = "./favicon.ico"
        client_socket.send(response.encode('utf-8'))    

    elif ".php" in file_path:
        print("PHP file detected")
        if request_type == "GET" or request_type == "get":
            Methode_array = requested_file.split("?")
            
            if len(Methode_array) > 1:
                elements = """array("""
                Methode_array = Methode_array[1].split('&')
                i=0
                while i < len(Methode_array)-1:
                    elements += f"\"{Methode_array[i].split('=')[0]}\""
                    elements += "=>"
                    elements += f"\"{Methode_array[i].split('=')[1]}\""
                    if i != len(Methode_array) - 1:
                        elements += ", "
                    i+=1
                elements += ")"

                try:
                    print(Methode_array)
                

                    f = open("Tempory_file.php", 'w')
                    f.writelines(f"""
                <?php
                    $_GET={elements};

                    include_once '{file_path}';
                ?>
                                """)
                    f.close()
                    php_output = subprocess.check_output(["./php/php.exe", "Tempory_file.php"], stderr=subprocess.STDOUT,cwd="./")
                    response = f"""HTTP/1.1 200 OK\nContent-Type: text/html\n\n{php_output.decode('utf-8')}"""
                    print(response)
                    client_socket.send(response.encode('utf-8'))
                except subprocess.CalledProcessError as e:
                    error_message = e.output.decode('utf-8')
                    response = f"""HTTP/1.1 500 Internal Server Error\nContent-Type: text/html\n\nInternal Server Error:<br>{error_message}"""
                    client_socket.send(response.encode('utf-8'))
            else:
                print(file_path)
                php_output = subprocess.check_output(["./php/php.exe", file_path], stderr=subprocess.STDOUT,cwd="./")
                response = f"""HTTP/1.1 200 OK\nContent-Type: text/html\n\n{php_output.decode('utf-8')}"""
                print(php_output)
                client_socket.send(response.encode('utf-8'))



        elif request_type == "POST" or request_type == "post":
            value_array = request.split('\n')[-1]
            #print(value_array('\n')[-1])
            Methode_array=value_array.split('&')
            if len(Methode_array) > 1:
                elements = """array("""
                import_file_path=request.split(' ')[1]
                # print(import_file_path)
                i=0
                while i < len(Methode_array)-1:
                    elements += f"\"{Methode_array[i].split('=')[0]}\""
                    elements += "=>"
                    elements += f"\"{Methode_array[i].split('=')[1]}\""
                    if i != len(Methode_array) - 1:
                        elements += ", "
                    i+=1
                elements += ")"

                try:
                    print(Methode_array)

                    f = open("Tempory_file.php", 'w')
                    f.writelines(f"""
                <?php
                    $_POST={elements};

                    include_once './htdocs{import_file_path}';
                ?>
                                """)
                    f.close()
                    php_output = subprocess.check_output(["./php/php.exe", "Tempory_file.php"], stderr=subprocess.STDOUT,
                                                         cwd="./")
                    response = f"""HTTP/1.1 200 OK\nContent-Type: text/html\n\n{php_output.decode('utf-8')}"""
                    client_socket.send(response.encode('utf-8'))
                except subprocess.CalledProcessError as e:
                    error_message = e.output.decode('utf-8')
                    response = f"""HTTP/1.1 500 Internal Server Error\nContent-Type: text/html\n\nInternal Server Error:<br>{error_message}"""
                    client_socket.send(response.encode('utf-8'))

            else:
                
                php_output = subprocess.check_output(["./php/php.exe", file_path], stderr=subprocess.STDOUT,cwd="./")
                response = f"""HTTP/1.1 200 OK\nContent-Type: text/html\n\n{php_output.decode('utf-8')}"""
                print(response)
                client_socket.send(response.encode('utf-8'))

    else:
        response = 'HTTP/1.1 404 Not Found\r\n\r\nFile Not Found'
        client_socket.send(response.encode('utf-8'))
    client_socket.close()

def main():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified host and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Listening on {HOST}:{PORT}")

    while True:
        # Accept incoming connections
        client_socket, addr = server_socket.accept()
         
        print("Accepted connection ")
        
        # Handle the client's request in a separate thread
        handle_client(client_socket)

if __name__ == '__main__':
    main()



