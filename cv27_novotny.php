<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Formulář</title>
    </head>
    <body>
    <?php

$db_host = "localhost";
$db_user = "root";
$db_pass = "root";
$db_db = "cv27";

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
    
      
    }
    $vek = $datum - $narozeni;
    $rch = rand(0, 4);

    $sql = "SELECT "$rch" FROM studenti";
            $result = $conn->query($sql);
            $data = [];

                }
            }
    $lnegth = strtolower($_POST['jmeno']);

    echo($jmeno);
    echo($narozeni);
    echo("Délka jména je", $length);
?>
</body>
</html>