import socket
import re 
import base64 

def decode(encoded_string):
    # Décodage de la chaîne Base64
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')

    # Affichage du résultat décodé
    print(f"Decoded string: {decoded_string}")
    return decoded_string

# Créer un socket TCP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Lier le socket à une adresse et un port
server_address = ('challenge01.root-me.org', 52023)
sock.connect(server_address)

try:
    while True :
        # Réception des données
        data = sock.recv(1024).decode()
        print(f"Raw data: {repr(data)}")


        # Utilisation d'expression régulière pour trouver la chaîne de caractères encodée
        match = re.search(r"my string is\s+'([^']+)'", data)

        
        if match:
            encoded_string = match.group(1)  # Extraction de la chaîne encodée

            # Effectuer le décodage
            resultat = decode(encoded_string)
            # Préparer la chaîne avec les caractères de terminaison "\r\n"
            message = str(resultat) + "\r\n"

            # Envoyer le message au serveur
            sock.send(message.encode())
            print(f"Envoyé: {resultat}")
        else:
            print("Aucune chaîne encodée trouvée dans les données reçues.")

finally:
    # Fermer la connexion
    sock.close()

