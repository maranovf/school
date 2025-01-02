<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Formulář</title>
    </head>
    <body>
    <?php

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
$vek = $datum - $narozeni;
echo $jmeno;
echo $narozeni;
echo $vek;
?>
</body>
</html>