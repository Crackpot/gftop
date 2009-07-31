<?php
$a = 2;
$b = 2;

echo '$a = '.$a;
echo '<br/>';
echo '$b = '.$b;
echo '<br/>';
echo '<br/>';

if($a<$b)
    echo '$a小于$b';
elseif($a>$b)
    echo '$a大于$b';
elseif($a==$b)
    echo '$a等于$b';
else
    'error!';
?>
