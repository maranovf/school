<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Přihlášení</title>
    </head>
    <body>
    <?php

$db_host = "localhost";
$db_user = "root";
$db_pass = "root";
$db_db = "";

$conn = new mysqli($db_host,$db_user,$db_pass,$db_db);
if($conn->connect_errno){
    echo "Chyba při připojování k databázi.".$conn->connect_error;
    exit();
}
$conn->set_charset("utf8");

    $jmeno = (isset($_POST['jmeno'])) ? $_POST['jmeno'] : '';
    $narozeni = (isset($_POST['narozeni'])) ? $_POST['jmeno'] : '';
?>

<form method="POST">
    <table>
        <tr>
            <td>Vaše jméno</td>
            <td><input name="jmeno" type="text" value="<?= htmlspecialchars($jmeno) ?>" required /></td>
        </tr>
        <tr>
            <td>Rok narození</td>
            <td><input name="narozeni" type="date" value="<?= htmlspecialchars($narozeni) ?>" required /></td>
        </tr>
        <tr>
            <td>Email</td>
            <td><input name="email" type="email" value="<?= htmlspecialchars($email) ?>" required /></td>
        </tr>
    </table>
    <input type="submit" value="Odeslat" />
</form>
<?php
date_default_timezone_set('Europe/Prague');
$datum = date('d. m. Y');

if(isset($_POST["jmeno"])){
    if(isset($_POST["narozeni"])){
    
      
      if($username == ""){
          $errors['jmeno'] = false;
      }
    
      if($password == ""){
        $errors['narozeni'] = false;
      }
      if($email == ""){
        $errors['email'] = false;
      }
      
    }
}

    $length = strtolower($_POST['jmeno']);

    echo($length);
    echo($narozeni);
    echo($email);
?>
</body>
</html>