<?php
    $i = "abc";
    $$i = "xyz";
    //新创建了一个变量$abc。上面这句相当于$abc = "xyz";

    echo "\$i=".$i;
    echo "<br/>";
    echo "<br/>";

    echo "$\$i=".$abc;
?>
