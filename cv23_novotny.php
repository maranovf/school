<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Kontaktní formulář</title>
    </head>
    <body>
     <form method="post">
         Jméno: <input type="text" name="jmeno" required><br>
         Email <input type="text" name="mail" required><br>
         <input type="submit" name="send" value="Odeslat">
     </form>
    </body>
</html>
<?php
$servername = "localhost";
$username = "root";
$password = "root";

$conn = new mysqli($servername, $username, $password);

$username01 = strtolower($_POST['jmeno']);
$mail01 = strtolower($_POST['jmeno']);

if(isset($_POST["login"])){
$username01 = strtolower($_POST['jmeno']);

  
  if($username01 == ""){
      $errors['jmeno'] = false;
  }

  if(mail01 == ""){
    $errors['jmeno'] = false;
  }

  
}
$delka = mb_strlen($username01);
if ($delka > 5){
    echo ("Jméno je delší než 5 znaků.");
}
echo ($username01);
echo ($mail01);

?>
