<?php
function say_hello($some_name)
{
    echo "Hello,".$some_name;
    echo "<br/>";
    echo "<br/>";
}

say_hello("Jenny");    //这里使用参数“Jenny”调用函数say_hello
say_hello("Harry");
say_hello("Ema");
?>