from pymongo import MongoClient

# URL de connexion MongoDB Atlas
uri = "mongodb+srv://faelby:<2NUEp2jDCcd3kod7>@cluster0.5bsuhkg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def connect_to_mongodb():
    try:
        # Connexion à MongoDB
        client = MongoClient(uri)

        # Accès à la base de données (remplacez 'votre_base_de_donnees' par le nom réel de votre base de données)
        db = client.ClashDesRaquettes

        # Test de la connexion en listant les collections
        collections = db.list_collection_names()
        print("Connexion réussie ! Collections disponibles :")
        for collection in collections:
            print(f"- {collection}")

        # Retourner la référence de la base de données pour d'autres opérations
        return db

    except Exception as e:
        print("Échec de la connexion à MongoDB Atlas : ", e)
        return None

if __name__ == "__main__":
    # Connexion à MongoDB et récupération de la base de données
    db = connect_to_mongodb()