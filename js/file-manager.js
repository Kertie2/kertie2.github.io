var username;
var password;
var token;
var repoOwner;
var repoName;

function login() {
    username = document.getElementById("username").value;
    password = document.getElementById("password").value;

    // Récupération du jeton d'accès à l'API GitHub
    getToken();

    // Récupération du propriétaire du référentiel et du nom du référentiel
    getRepoDetails();

    // Vérification des informations d'identification
    // (Vous pouvez utiliser votre propre logique d'authentification ici)
    if (username === "admin" && password === "admin") {
        // Affichage du gestionnaire de fichiers après la connexion réussie
        document.getElementById("loginForm").style.display = "none";
        document.getElementById("fileManager").style.display = "block";
        displayFiles();
    } else {
        alert("Nom d'utilisateur ou mot de passe incorrect.");
    }
}

function getToken() {
    // Appel à l'API GitHub pour obtenir un jeton d'accès
    // Remplacez `YOUR_CLIENT_ID` et `YOUR_CLIENT_SECRET` par vos propres informations d'authentification
    fetch("https://github.com/login/oauth/access_token", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        body: JSON.stringify({
            client_id: "2fb1ead3d8dc48de958b",
            client_secret: "67156d6042b1a8ec4ad93b477055be80a23172a5",
            code: "f8be85ec6e72ce79d9e5"
        })
    })
    .then(response => response.json())
    .then(data => {
        token = data.access_token;
    })
    .catch(error => {
        console.error("Erreur lors de la récupération du jeton d'accès:", error);
    });
}

function getRepoDetails() {
    // Appel à l'API GitHub pour obtenir les détails du référentiel
    // Remplacez `YOUR_REPO_FULL_NAME` par le nom complet de votre référentiel (ex: "owner/repo")
    fetch("https://api.github.com/repos/Kertie2/kertie2.github.io", {
        headers: {
            "Authorization": "token " + token
        }
    })
    .then(response => response.json())
    .then(data => {
        repoOwner = data.owner.login;
        repoName = data.name;
    })
    .catch(error => {
        console.error("Erreur lors de la récupération des détails du référentiel:", error);
    });
}

function displayFiles() {
    var fileList = document.getElementById("fileList");
    fileList.innerHTML = "";

    // Appel à l'API GitHub pour obtenir la liste des fichiers du référentiel
    fetch("https://api.github.com/repos/" + repoOwner + "/" + repoName + "/contents", {
        headers: {
            "Authorization": "token " + token
        }
    })
    .then(response => response.json())
    .then(data => {
        // Affichage des fichiers
        for (var i = 0; i < data.length; i++) {
            var file = data[i];
            var fileItem = document.createElement("div");
            fileItem.innerHTML = file.name;
            fileList.appendChild(fileItem);
        }
    })
    .catch(error => {
        console.error("Erreur lors de la récupération des fichiers:", error);
    });
}

function uploadFile() {
    var fileInput = document.getElementById("fileInput");
    var file = fileInput.files[0];

    var reader = new FileReader();
    reader.onload = function (event) {
        var content = event.target.result;

        // Appel à l'API GitHub pour créer ou mettre à jour le fichier
        fetch("https://api.github.com/repos/" + repoOwner + "/" + repoName + "/contents/" + file.name, {
            method: "PUT",
            headers: {
                "Authorization": "token " + token,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: "Nouveau fichier",
                content: btoa(content) // Conversion du contenu en base64
            })
        })
        .then(response => response.json())
        .then(data => {
            alert("Fichier téléchargé avec succès.");
            displayFiles(); // Mettre à jour la liste des fichiers après le téléchargement
        })
        .catch(error => {
            console.error("Erreur lors du téléchargement du fichier:", error);
        });
    };
    reader.readAsText(file);
}
