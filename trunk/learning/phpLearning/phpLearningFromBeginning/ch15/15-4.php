<?php
$str = "You have a car, I have a Car, We have cARs!";
echo "<b>�滻ǰ�ַ���Ϊ��</b><br/>";
echo $str;
echo "<br/>";
echo "<br/>";

$pattern = "car";
$replacement = "Apple";
$str_rpc = eregi_replace($pattern, $replacement, $str);
echo "<b>�滻���ַ���Ϊ��</b><br/>";
echo $str_rpc;
?>