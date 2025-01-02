<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<?php
$jmeno = (isset($_POST['jmeno'])) ? $_POST['jmeno'] : '';
?>
<form method="post" $_SERVER["PHP_SELF"]>
         Jméno: <input type="text" name="jmeno" required><br>;
         Datum: <input type="date" name="datum" required><br>
         Email: <input type="text" name="email" required><br>
         <input type="submit" name="send" value="Přihlásit se">
     </form>
    </body>
</body>
</html>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
}
$pocet = count($_POST[$jmeno]);
if (empty($_POST["datum"])) {
if (empty($_POST["email"])) {
}
}
else {
}
echo $_POST["jmeno"];
echo $_POST["datum"];
echo $_POST["email"];
?>