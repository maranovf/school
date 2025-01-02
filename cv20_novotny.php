<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Page Title</title>
    </head>
    <body>
    <?php
    $pole = ['Jan','Pepa','Franta', "Marek", "Jirka"];
    $pocet = count($pole);

    if($pocet > 4){
        echo "Velké pole";
    }
    else{
        echo "Malé pole";
    }
?>
</body>
</html>