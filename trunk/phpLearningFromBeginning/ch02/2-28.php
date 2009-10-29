<?php
    $i = 1;
    $sum = 0;

    do
    {
        $sum = $sum + $i;
        $i ++;
    }
    while($i <= 100);

    echo "1 + 2 + 3 +...+ 99 + 100 = ".$sum;
?>
