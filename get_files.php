<?php
$files = scandir($_SERVER['DOCUMENT_ROOT']);
$files = array_diff($files, array('.', '..')); // Supprime les entrées '.' et '..'

echo json_encode(array_values($files));
?>
