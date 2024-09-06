import socket
import codecs  # Import nécessaire pour ROT13

host = "challenge01.root-me.org"
port = 52021

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((host, port))
    question = client_socket.recv(1024).decode()
    print(question)
    
    # Extraction de la chaîne encodée à partir du message
    search = question.split("'")
    code = search[1]
    
    # Décodage ROT13
    result = codecs.decode(code, 'rot_13')  # Utilisation de codecs pour ROT13
    print(f"Décodé = {result}")
    
    # Préparation et envoi de la réponse
    send_rep = (str(result) + "\n").encode()
    client_socket.send(send_rep)
    
    # Réception de la réponse du serveur
    flag = client_socket.recv(1024).decode()
    print(flag)

finally:
    # Fermeture de la connexion
    client_socket.close()
