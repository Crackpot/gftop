<?php
    $item = 43;
    echo "item=$item,其类型为：".gettype($item)."<br/>";
    echo "变量item是array类型：".is_array($item)."<br/>";
    echo "变量item是integer类型：".is_integer($item)."<br/>";
    echo "变量item是double类型：".is_double($item)."<br/>";
    echo "变量item是numeric类型：".is_numeric($item)."<br/>";
?>
