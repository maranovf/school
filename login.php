<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Přihlášení uživatele</title>
    </head>
    <body>
     <form method="post">
         Uživatelské jméno: <input type="text" name="jmeno" required><br>
         Heslo: <input type="password" name="password" required><br>
         <input type="submit" name="send" value="Přihlásit se">
     </form>
    </body>
</html>
<?php
$servername = "localhost";
$username = "root";
$password = "root";

$conn = new mysqli($servername, $username, $password);

if(isset($_POST["login"])){
$username = strtolower($_POST['jmeno']);

  
  if($username == ""){
      $errors['jmeno'] = false;
  }

  if($password == ""){
    $errors['jmeno'] = false;
  }

  
}

?>
