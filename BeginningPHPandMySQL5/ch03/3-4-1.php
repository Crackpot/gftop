<title>标量数据类型</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<h3>1.布尔型</h3>
<?php
    $alive = false; # $alive is false. 不显示
    echo "alive = $alive"."<br/>";
    $alive = 1; # $alive is true. 
    echo "alive = $alive"."<br/>";
    $alive = -1; # $alive is true. 
    echo "alive = $alive"."<br/>";
    $alive = 5; # $alive is true. 
    echo "alive = $alive"."<br/>";
    $alive = 0; # $alive is false. 
    echo "alive = $alive"."<br/>";
?>

<h3>2.整型</h3>
<?php
    $val = 42; # decimal
    echo "val = $val"."<br/>";
    $val = -678900; # decimal
    echo "val = $val"."<br/>";
    $val = 0755; # octal 493
    echo "val = $val"."<br/>";
    $val = 0xC4E; # hexadecimal 3150
    echo "val = $val"."<br/>";
    $val = 45678945939390393678976; # decimal 4.567894593939E+22
    $val = $val + 5;
    echo "val = $val"."<br/>";
?>

<h3>3.浮点型</h3>
<?php
    $val = 4.5678; # 4.5678
    echo "val = $val"."<br/>";
    $val = 4.0; # 4
    echo "val = $val"."<br/>";
    $val = 8.7e4; # 87000 
    echo "val = $val"."<br/>";
    $val = 1.23E+11; # 123000000000  
    echo "val = $val"."<br/>";
    $val = 1.23E-11; # 1.23E-11 
    echo "val = $val"."<br/>";
?>

<h3>4.字符串</h3>
<?php
    $str = "whoop-de-do";
    echo "str = $str"."<br/>";
    $str = "sunday\n";
    echo "str = $str"."<br/>";
    $str = "123$%^789";
    echo "str = $str"."<br/>";

    $color = "maroon";
    echo "color = $color"."<br/>";
    echo "color[0] = $color[0]"."<br/>";
    echo "color[3] = $color[3]"."<br/>";
?>
