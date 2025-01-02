<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Data</title>
    </head>
    <body>
    <?php
    $data = ["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"];
    $poradi = rand(0, 6);
    $chosen_one = $data[$poradi];
    echo $chosen_one;
    $pocet = mb_strlen($chosen_one);
    echo $pocet;
    echo count($data);
    ?>
    </body>
    </html>