import os;

def main():

    #nom = input('donnez votre nom \n')
    nom= 'Tortue Genial'

    fichier = "fichier.txt"

    if os.path.exists(fichier):
        with open(fichier,'a') as f:
            f.write(f'Bonjour {nom} !\n')
        print('fichier mise a jour')
    else:
        print("le fichier n'existe pas")

if __name__ == "__main__":
    main()