<?php
$a = 1997;
$b = 1998;

function sum()
{
    global $a,$b;
    $b = $a + $b;
}

echo '$a='.$a;
echo '<br/>';
echo '$b='.$b;
echo '<br/>';
echo '<br/>';

sum();
echo '$a + $b = '.$b;
?>