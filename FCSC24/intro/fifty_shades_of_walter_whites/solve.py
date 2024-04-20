import socket
import time
import string

def recv_bis(clientt, printout=True, size=4096):
       data = clientt.recv(size)
       datastr =data.decode("utf-8")
       if printout : print(datastr, end="")
       return datastr

def send_check(clientt, msg):
    #print(msg+"\n")
    n = clientt.send((msg+"\n").encode("utf-8"))
    if (n != len((msg+"\n"))):
            print( 'Erreur envoi.')

if __name__ == "__main__":

    HOST = 'challenges.france-cybersecurity-challenge.fr'
    PORT = 2250

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print( 'Connexion vers ' + HOST + ':' + str(PORT) + ' reussie.')

    #Wait for the connection message
    time.sleep(3)
    # Ajust the size of the message depending on what the server sends back, don't forget to put \n !
    size_r = len("stringsnethere")
    recv_bis(client, size=size_r)

    # Message to send (don't forget the \n at the end of the message)
    message = """----BEGIN WHITE LICENSE----
    TmFtZTogV2FsdGVyIFdoaXRlIEp1bmlvcgpTZXJpYWw6IDFkMTE3YzVhLTI5N2QtNGNlNi05MTg2LWQ0Yjg0ZmI3ZjIzMApUeXBlOiAxMzM3Cg==
    -----END WHITE LICENSE-----\n"""
    send_check(client, message)

    recv_bis(client)

    print( 'Deconnexion.')
    client.close()