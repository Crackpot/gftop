<?php
    $a = 100;

    echo "设置前，变量\$a的类型是：".gettype($a);
    echo "<br/>";
    echo "<br/>";

    settype($a,"string");
    echo "设置后，变量\$a的类型是：".gettype($a);
?>
