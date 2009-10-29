<?php
    $i = 100;

    function func($n)#传递参数的值
    {
        $n = $n + 100;
    }

    echo "调用函数func前：\$i = $i"."<br/>";
    echo "<br/>";

    func($i);#调用函数
    echo "调用函数func后：\$i = $i"."<br/>";
?>
