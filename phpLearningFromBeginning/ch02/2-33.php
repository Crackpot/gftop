<?php
function say_hello($some_name = "Jack")
{
    echo "Hello,".$some_name;
    echo "<br/>";
    echo "<br/>";
}

say_hello();           //不使用任何参数调用函数say_hello时，函数将使用函数定义的默认参数“Jack”
say_hello("Jenny");    //使用参数“Jenny”调用函数say_hello
say_hello("Harry");
say_hello("Ema");
?>