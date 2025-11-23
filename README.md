# ue19-lab-05
# Oracle des Âges (Agify Client)

![Badge Statut](https://img.shields.io/badge/Status-Fonctionnel-brightgreen) ![Badge Python](https://img.shields.io/badge/Python-3.x-blue)

## Description

L'**Oracle des Âges** est une application légère en ligne de commande (CLI) écrite en Python. Elle utilise l'API publique [Agify.io](https://agify.io/) pour prédire l'âge moyen d'une personne en se basant uniquement sur son prénom.

Ce projet a été créé pour démontrer comment effectuer des requêtes HTTP simples et manipuler des données JSON avec la librairie `requests`.

### Pourquoi ce projet ?
L'objectif est de fournir un exemple clair et éducatif sur :
- L'interrogation d'une API REST publique.
- La gestion des erreurs de connexion.
- Le parsing (analyse) d'une réponse JSON.

## Fonctionnalités

- **Prédiction d'âge :** Obtient l'âge moyen estimé pour n'importe quel prénom.
- **Statistiques :** Affiche le nombre de personnes sur lequel la prédiction est basée (taille de l'échantillon).
- **Gestion d'erreurs :** Gère gracieusement les erreurs de réseau ou les réponses invalides de l'API.
- **Interface Simple :** Interaction directe via le terminal.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé Python 3 sur votre machine.

## Installation

1. **Cloner le projet** (ou télécharger le fichier `.py`) :
   ```bash
   git clone [https://github.com/votre-utilisateur/oracle-des-ages.git](https://github.com/votre-utilisateur/oracle-des-ages.git)
   cd oracle-des-ages
