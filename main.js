const {google} = require('googleapis');

exports.handler = async function(event, context) {
    // Récupérer l'email à partir de la requête
    const email_to_add = event.queryStringParameters.email;

    // Chemin vers le fichier de clé du compte de service
    const keyFile = 'newsletter-410220-5dc4f904e977.json';

    // Construire le service d'authentification
    const auth = new google.auth.GoogleAuth({
        keyFile: keyFile,
        scopes: ['https://www.googleapis.com/auth/admin.directory.group.member']
    });
    const authClient = await auth.getClient();
    const service = google.admin({version: 'directory_v1', auth: authClient});

    // Ajouter l'email au groupe Google
    const groupKey = 'newsletter-one-piece-phoenix@newsletter-410220.iam.gserviceaccount.com';
    const res = await service.members.insert({
        groupKey: groupKey,
        requestBody: {
            email: email_to_add,
            role: 'MEMBER'
        }
    });

    return {
        statusCode: 200,
        body: JSON.stringify({message: "Email ajouté avec succès au groupe !"})
    };
}

