<?php
    $var = "some text";
    echo '这是函数外的变量$var：'.$var."<br/>";

    function test()
    {
        $var = "some text in function";
        echo '这是函数内的局部变量$var：'.$var."<br/>";
    }

    echo '这是全局变量$var：'.$var."<br/>";
    echo '<br/>';
    test();
?>
