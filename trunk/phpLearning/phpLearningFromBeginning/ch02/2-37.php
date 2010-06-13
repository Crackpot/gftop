<?php
    $var = "some text";
    echo "这是函数外的变量\$var:".$var."<br/>";

    function test()
    {
        echo "这是调用函数的结果："."<br/>";
        echo $var;
    }

    test();
?>
