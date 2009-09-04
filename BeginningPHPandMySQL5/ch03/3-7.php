<h3>常量</h3>
<?php
    define("PI",3.1415926);
    echo "常量前加美元符号无效"."<br/>";
    echo "\$PI = $PI"."<br/>";
    echo "PI = PI"."<br/>";
    echo "PI = ".PI."<br/>";
    $pi2 = 2 * PI;
?>
<?php
    if(!$_POST['banjing']){
?>
    <form action="3-7.php" method="POST">
        <p>
            圆的半径：<input type="text" name="banjing" maxlength="30">
        </p>
        <p>
            <input type="submit" name="submit" value="计算圆的周长和面积">
        </p>
    </form>
<?php
    }
    if($_POST['banjing']){
        echo "<p>圆的周长是：".(2*PI*$_POST['banjing'])."</p>";
        echo "<p>圆的面积是：".(PI*$_POST['banjing']*$_POST['banjing'])."</p>";
    }
?>
<a href="./">返回</a>
