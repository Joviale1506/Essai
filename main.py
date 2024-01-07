from flask import Flask, request
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = Flask(__name__)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    # Récupérer l'email à partir de la requête
    email_to_add = request.form.get('email')

    # Chemin vers le fichier de clé du compte de service
    key_file = 'C:\\Users\\Joviale\\IdeaProjects\\Newsletter\\newsletter-410220-5dc4f904e977.json'

    # Construire le service d'authentification
    credentials = service_account.Credentials.from_service_account_file(
        key_file,
        scopes=['https://www.googleapis.com/auth/admin.directory.group.member']
    )
    service = build('admin', 'directory_v1', credentials=credentials)

    # Ajouter l'email au groupe Google
    group_key = 'newsletter-one-piece-phoenix@newsletter-410220.iam.gserviceaccount.com'
    service.members().insert(
        groupKey=group_key,
        body={
            'email': email_to_add,
            'role': 'MEMBER'
        }
    ).execute()

    return 'Email ajouté avec succès au groupe !'

if __name__ == '__main__':
    app.run(debug=True)
