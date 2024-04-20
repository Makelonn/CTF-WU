import socket
import time

def send_message(host, port, message):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        s.connect((host, port))
        time.sleep(1)

        # Send the message
        s.sendall(message.encode())

        # Receive and print data from the server
        while True:
            response = s.recv(1024)
            if not response:
                break
            print("Response from server:", response.decode())

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the socket
        s.close()

if __name__ == "__main__":
    # Server details
    host = "challenges.france-cybersecurity-challenge.fr"
    port = 2250

    # Message to send
    message = """----BEGIN WHITE LICENSE----
    TmFtZTogV2FsdGVyIFdoaXRlIEp1bmlvcgpTZXJpYWw6IDFkMTE3YzVhLTI5N2QtNGNlNi05MTg2LWQ0Yjg0ZmI3ZjIzMApUeXBlOiAxMzM3Cg==
    -----END WHITE LICENSE-----"""

    # Call the function to send the message
    send_message(host, port, message)
    send_message(host, port, message)
    send_message(host, port, message)
    send_message(host, port, message)
    send_message(host, port, message)
    
