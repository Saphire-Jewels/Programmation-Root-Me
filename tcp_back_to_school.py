import socket
import math
import re

def calcul(nombre1, nombre2):
    # Calcul de la racine carrée de nombre1
    racine_carree = math.sqrt(nombre1)
    
    # Multiplier le résultat par nombre2
    resultat = racine_carree * nombre2
    
    # Arrondir le résultat à deux chiffres après la virgule
    resultat_arrondi = round(resultat, 2)
    
    return resultat_arrondi

# Créer un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se connecter à un serveur
server_address = ('challenge01.root-me.org', 52002)
sock.connect(server_address)

try:
    while True:
        # Réception des données
        data = sock.recv(1024).decode()
        print(f"Reçu: {data}")

        # Utilisation d'expressions régulières pour trouver les nombres après les mots-clés spécifiques
        match_n1 = re.search(r'square root of (\d+)', data)
        match_n2 = re.search(r'multiply by (\d+)', data)

        if match_n1 and match_n2:
            n1 = float(match_n1.group(1))
            n2 = float(match_n2.group(1))

            # Effectuer le calcul
            resultat = calcul(n1, n2)

            # Préparer la chaîne avec les caractères de terminaison "\r\n"
            message = str(resultat) + "\r\n"

            # Envoyer le message au serveur
            sock.send(message.encode())
            print(f"Envoyé: {resultat}")

            # Recevoir la réponse du serveur après avoir envoyé le message
            response = sock.recv(4096).decode()
            print(f"Réponse du serveur: {response}")

        else:
            print("Impossible de trouver les nombres dans le message reçu.")
            break

finally:
    # Fermer la connexion
    sock.close()
