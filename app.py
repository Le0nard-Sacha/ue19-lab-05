import requests


def deviner_age():
    print("--- Oracle des Âges ---")
    prenom = input("Entrez un prénom : ")
    url = f"https://api.agify.io?name={prenom}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            age = data.get('age')
            compte = data.get('count')

            if age is None:
                print(f"Désolé, je n'ai pas assez de données pour le prénom '{prenom}'.")
            else:
                print(f"\nSelon mes données (basées sur {compte} personnes)...")
                print(f"L'âge moyen pour '{prenom}' est de : {age} ans.")
        else:
            print(f"Erreur lors de l'appel à l'API (Code: {response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"Une erreur de connexion est survenue : {e}")
if __name__ == "__main__":
    deviner_age()