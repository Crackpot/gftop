<h3>变量的声明</h3>
<h5>几个变量声明的例子</h5>
<?php
    $color = "green";
    echo "color = $color"."<br/>";
    $operating_system = "OpenSUSE 11.1";
    echo "operating_system = $operating_system"."<br/>";
    $_some_variable = "下划线变量名";
    echo "_some_variable = $_some_variable"."<br/>";
    $model = "模型";
    echo "model = $model"."<br/>";
?>
<h5>变量名是区分大小写的</h5>
<?php
    $color = "red";
    echo "color = $color"."<br/>";
    $Color = "yellow";
    echo "Color = $Color"."<br/>";
    $COLOR = "blue";
    echo "COLOR = $COLOR"."<br/>";
?>

<h4>1、值赋值</h4>
<?php
    $color = "red";
    echo "color = $color"."<br/>";
    $number = 12;
    echo "number = $number"."<br/>";
    $age = 23;
    echo "age = $age"."<br/>";
    $sum = 12 + "15";
    echo "sum = $sum"."<br/>";
?>

<h4>2、引用赋值</h4>
<?php
    $value1 = "Hello";
    echo "value1 = $value1"."<br/>";
    $value2 =& $value1;
    echo "value2 = value1 = $value2"."<br/>";
    $value1 = "Hello world";
    echo "value1 = $value1"."<br/>";
    echo "更改了value1的值之后value2的值也发生变化"."<br/>";
    echo "value2 = $value2"."<br/>";
    $value2 = "Goodbye";
    echo "value2 = $value2"."<br/>";
    $value1 = &$value2;
    echo "value1 = value2 = $value1"."<br/>";
?>
