<?php
    function say_hello()
    {
        $name = "Jack";
        echo "Hello,".$name."<br/>";
        echo "这是调用了say_hello函数的结果"."<br/>";
    }

    say_hello();    //这里调用上面定义的函数say_hello
?>
