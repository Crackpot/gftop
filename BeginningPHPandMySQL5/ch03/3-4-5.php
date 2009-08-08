<?php
    $total = 5;
    echo "total = $total"."&nbsp;&nbsp;&nbsp;数值型变量"."<br/>";
    $count = "15";
    echo "count = $count"."&nbsp;&nbsp;&nbsp;字符串型变量"."<br/>";
    $total += $count;
    echo "total = total + count = $total"."&nbsp;&nbsp;&nbsp;字符串变量会自动转换成整数型变量参与运算"."<br/>"; // $total = 20



    echo "<br/>";
    $total = "45 fire engines";
    echo "total = $total"."<br/>";
    $incoming = 10;
    echo "incoming = $incoming"."<br/>";
    $total = $incoming + $total; // $total = 55
    echo "total = incoming +total = $total"."&nbsp;&nbsp;&nbsp;total字符串以整数值开头，在计算中就使用了这个整数值"."<br/>"; // total = 55



    echo "<br/>";
    $total = "1.0";
    echo "total = $total"."<br/>";
    if($total){
        echo "The total count is positive"."<br/>";
    }
    echo "为了计算if语句的值，字符串被转换为布尔类型"."<br/>";


    echo "<br/>";
    $val1 = "1.2e13";
    echo "val1 = $val1"."<br/>";
    $val2 = 2;
    echo "val2 = $val2"."<br/>";
    echo "浮点数和整数的四则运算，会将浮点数转换成为整数类型："."<br/>";
    $val3 = $val1 + $val2;
    echo "val3 = val1 + val2 = $val3"."<br/>";
    $val3 = $val1 - $val2;
    echo "val3 = val1 - val2 = $val3"."<br/>";
    $val3 = $val1 * $val2;
    echo "val3 = val1 * val2 = $val3"."<br/>";
    $val3 = $val1 / $val2;
    echo "val3 = val1 / val2 = $val3"."<br/>";
?>
