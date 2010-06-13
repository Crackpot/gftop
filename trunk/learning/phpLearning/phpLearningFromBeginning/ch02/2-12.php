<?php
    $var = "Test string";
    echo "变量var值为：".$var."<br/>";
    echo "删除变量var"."<br/>";
    unset($var);                 //删除单个变量
    echo "变量var值为：".$var."<br/>";

    echo "<br/>";

    $arr['elem']="Test string";
    echo "数组arr中elem下标的元素为：".$arr["elem"]."<br/>";
    echo "删除数组arr中elem下标的元素"."<br/>";
    unset($arr['elem']);         //删除单个数组元素
    echo "数组arr中elem下标的元素为：".$arr["elem"]."<br/>";

    echo "<br/>";

    $var1 = 1;$var2 = 2;$var3 = 3;
    echo "变量var1的值为：".$var1."<br/>";
    echo "变量var2的值为：".$var2."<br/>";
    echo "变量var3的值为：".$var3."<br/>";
    echo "同时删除变量var1,var2,var3"."<br/>";
    unset($var1, $var2, $var3);  //删除一个以上的变量
    echo "变量var1的值为：".$var1."<br/>";
    echo "变量var2的值为：".$var2."<br/>";
    echo "变量var3的值为：".$var3."<br/>";
?>
