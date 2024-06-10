import requests
from bs4 import BeautifulSoup

# Informations de connexion
username = 
password = 

# URL de connexion
login_url = 'https://gitlab.sorbonne-universite.fr/users/sign_in'

# Démarrer une session
session = requests.Session()

# Obtenir la page de connexion pour extraire le jeton d'authenticité
login_page = session.get(login_url)
login_soup = BeautifulSoup(login_page.text, 'html.parser')
authenticity_token = login_soup.find('input', {'name': 'authenticity_token'}).get('value')

# Préparer les données de connexion
login_data = {
    'user[login]': username,
    'user[password]': password,
    'authenticity_token': authenticity_token
}

# Envoyer la requête de connexion
response = session.post(login_url, data=login_data)

# Vérifier si la connexion est réussie
if response.url == 'https://gitlab.sorbonne-universite.fr/':
    print('Connexion réussie.')
    '''
    # Exemple d'utilisation de la session pour créer un fichier
    file_path = 'chemin/vers/fichier'
    commit_message = 'Votre message de commit'
    branch_name = 'nom_de_la_branche'  # ex: 'main' ou 'master'
    project_id = 'votre_project_id'  # Vous pouvez obtenir cela à partir de l'URL du projet

    # Lire le contenu du fichier
    with open(file_path, 'rb') as file:
        content = base64.b64encode(file.read()).decode()

    # Préparer les données pour la requête
    data = {
        'branch': branch_name,
        'content': content,
        'commit_message': commit_message,
        'encoding': 'base64'
    }

    # Préparer l'URL pour créer/mettre à jour un fichier
    url = f'https://gitlab.sorbonne-universite.fr/api/v4/projects/{project_id}/repository/files/{file_path.replace("/", "%2F")}'

    # Envoyer la requête PUT pour créer/mettre à jour le fichier
    file_response = session.put(url, json=data)

    # Vérifier la réponse
    if file_response.status_code in [200, 201]:
        print('Fichier envoyé avec succès.')
    else:
        print(f'Échec de l\'envoi du fichier. Statut: {file_response.status_code}, Réponse: {file_response.json()}')
    '''
else:
    print('Échec de la connexion.')
