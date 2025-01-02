<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Page Title</title>
    </head>
    <body>      
        <h1>Seznam studentů</h1>
        <?php

            $db_host = "localhost";
            $db_user = "root";
            $db_pass = "root";
            $db_db = "studenti";

            $conn = new mysqli($db_host,$db_user,$db_pass,$db_db);
            if($conn->connect_errno){
                echo "Chyba při připojování k databázi.".$conn->connect_error;
                exit();
            }
            $conn->set_charset("utf8");

            $sql = "SELECT * FROM studenti";
            $result = $conn->query($sql);
            $datas = [];

            if($result){
                while($row = $result->fetch_assoc()){
                    $datas[] = $row;
                }
            }
            $result->free();
            ?>
            <ul>
                <?php foreach($datas as $student):?>
                    <li><?php echo $student['jmeno_prijmeni'];?></li>
                <?php endforeach;?>    
            </ul>
            
    </body>
</html>