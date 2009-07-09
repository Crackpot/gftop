<?php
$str = "You have a car, I have a Car, We have cARs!";
echo "<b>Ìæ»»Ç°×Ö·û´®Îª£º</b><br/>";
echo $str;
echo "<br/>";
echo "<br/>";

$pattern = "car";
$replacement = "Apple";
$str_rpc = eregi_replace($pattern, $replacement, $str);
echo "<b>Ìæ»»ºó×Ö·û´®Îª£º</b><br/>";
echo $str_rpc;
?>