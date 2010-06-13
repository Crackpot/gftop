<?php
    $s = "this is a string";
    echo "变量s：".$s."<br/>";
    $i = 9;
    echo "变量i：".$i."<br/>";
    $arr = array(2,4,6);
    echo "变量arr：".$arr."<br/>";
    
    echo "<br/>";
    echo "变量s是字符串：".is_string($s)."<br/>";    //返回TRUE，表示$s是一个字符串变量
    echo "变量s是数组：".is_array($s)."<br/>";     //返回FALSE，表示$s不是一个数组
    echo "变量i是整数：".is_int($i)."<br/>";    //返回TRUE，表示$i不是一个整型变量
    echo "变量i是字符串：".is_string($i)."<br/>";    //返回FALSE，表示$i不是一个字符串变量
    echo "变量arr是数组：".is_array($arr)."<br/>";   //返回TRUE，表示$arr是一个数组
?>
