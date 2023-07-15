<?php
// Récupération des informations d'identification envoyées depuis le formulaire
$username = $_POST['username'];
$password = $_POST['password'];

// Vérification des informations d'identification
if ($username === "admin" && $password === "password") {
  // Informations d'identification valides, démarrage de la session
  session_start();
  $_SESSION['admin'] = true;

  // Redirection vers la page d'accueil des administrateurs
  header('Location: admin_home.html');
  exit();
} else {
  // Identifiants incorrects, redirection vers la page de connexion avec un message d'erreur
  header('Location: login.html?error=1');
  exit();
}
?>
