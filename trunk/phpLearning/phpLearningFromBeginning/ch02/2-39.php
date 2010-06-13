<?php
    $a = 1997;
    $b = 1998;

    function sum()
    {
        global $a,$b;
        $b = $a + $b;
    }

    echo '$a='.$a."<br/>";
    echo '$b='.$b."<br/>";
    echo '<br/>';

    sum();
    echo '$a + $b = '.$b;
?>
