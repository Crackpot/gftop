<?php
$str1 = "PHP string";
$str2 = "PHP String";

if(strcmp($str1,$str2)==0)
{
    echo "$str1 �� $str2 ���";
    echo "<br/";
}
else
{
    echo "$str1 �� $str2 �����";
    echo "<br/>";
    echo "<br/>";
    echo "����strcmp�ıȽϽ��Ϊ��".strcmp($str1,$str2);
}
?>