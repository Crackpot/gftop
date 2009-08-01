<?php
    $var = "test string";
    echo "变量var定义过：".isset($var)."<br/>";  //$var定义过，返回TRUE
    echo "变量a定义过：".isset($a)."<br/>";    //$a未被定义，返回FALSE
?>
