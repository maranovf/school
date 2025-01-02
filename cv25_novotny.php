<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Výpis z databáze</title>
    </head>
    <body>
        <?php
            $servername = "localhost";
            $username = "root";
            $password = "root";
            $databaze = "studenti";
            
            $conn = new mysqli($servername, $username, $password, $databaze);

            $sql = "SELECT * FROM studenti";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
  while($row = mysqli_fetch_assoc($result)) {
    echo "" . $row["id"]. "" . $row["jmeno_prijmeni"]. " " . $row["datum_narozeni"]. " " . $row["trida"]. "<br>";
  }
} else {
  echo "0 výsledků";
}

mysqli_close($conn);
            ?>