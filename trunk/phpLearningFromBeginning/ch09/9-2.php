<?php
$i = 22;
$bi = 1011001;
$oi = 721;
$hi = A2;

echo "$i 的二进制数是：".decbin($i);
echo "<br/>";
echo "<br/>";
echo "$i 的八进制数是：".decoct($i);
echo "<br/>";
echo "<br/>";
echo "$i 的十六进制数是：".dechex($i);
echo "<hr>";

echo "二进制数 $bi 的十进制数是：".bindec($bi);
echo "<br/>";
echo "<br/>";
echo "八进制数 $oi 的十进制数是：".octdec($oi);
echo "<br/>";
echo "<br/>";
echo "十六进制数 $hi 的十进制数是：".hexdec($hi);
echo "<hr>";

$hex_num = 'A515';
echo "使用函数base_convert()，转换十六进制数B515到二进制数：<br/>";
echo base_convert($hex_num,16,2);
?>
