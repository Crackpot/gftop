<?php
    $a = 2;
    $b = 3;

    echo '$a = '.$a."<br/>";
    echo '$b = '.$b."<br/>";
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
