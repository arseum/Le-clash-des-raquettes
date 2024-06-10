from pymongo import MongoClient

# URL de connexion MongoDB Atlas
uri = ("mongodb+srv://faelby:<EpO1QKzA6pA23HqV>@cluster0.5bsuhkg.mongodb.net/?directConnection=true&retryWrites=true&w"
       "=majority&appName=Cluster0")


def connect_to_mongodb():
    try:
        client = MongoClient(uri)

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
    db = connect_to_mongodb()
