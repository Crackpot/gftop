<?php
$str1 = "PHP string";
$str2 = "PHP String";

if(strcmp($str1,$str2)==0)
{
    echo "$str1 和 $str2 相等";
    echo "<br/";
}
else
{
    echo "$str1 和 $str2 不相等";
    echo "<br/>";
    echo "<br/>";
    echo "函数strcmp的比较结果为：".strcmp($str1,$str2);
}
?>