<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Page Title</title>
    </head>
    <body>
    <?php
    $s = ['Jan','Pepa','Franta', "Marek", "Jirka"];
    $rando = rand(0, 4);
    $ch = ($s[$rando]);
    echo ($ch);
    $p = strlen($ch);
    echo ($p);
    echo count($s);
    ?>
    </body>
    </html>