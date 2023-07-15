function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Vérification des informations d'identification
    if (username === "admin" && password === "admin") {
        // Affichage du gestionnaire de fichiers après la connexion réussie
        document.getElementById("loginForm").style.display = "none";
        document.getElementById("fileManager").style.display = "block";
        displayFiles();
    } else {
        alert("Nom d'utilisateur ou mot de passe incorrect.");
    }
}

function displayFiles() {
    var fileList = document.getElementById("fileList");
    fileList.innerHTML = "";

    // Récupération de la liste des fichiers depuis le serveur (exemple statique)
    var files = ["document1.txt", "image.jpg", "music.mp3"];

    // Affichage des fichiers
    for (var i = 0; i < files.length; i++) {
        var file = files[i];
        var fileItem = document.createElement("div");
        fileItem.innerHTML = file;
        fileList.appendChild(fileItem);
    }
}
