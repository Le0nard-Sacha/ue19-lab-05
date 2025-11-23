# 1. Image de base : On part d'une version légère de Python 3
FROM python:3.9-slim

# 2. Dossier de travail : On crée un dossier /app dans le conteneur
WORKDIR /app

# 3. Gestion des dépendances :
# On copie d'abord le requirements.txt pour profiter du cache Docker
COPY requirements.txt .

# On installe les librairies nécessaires
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copie du code : On copie le reste des fichiers (app.py) dans le conteneur
COPY app.py .

# 5. Commande de démarrage : Ce qui se lance quand on démarre le conteneur
CMD ["python", "app.py"]
