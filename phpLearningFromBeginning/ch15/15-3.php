<?php
$str = "1fish2fish3fish4fish5fish";
echo "<b>Ìæ»»Ç°×Ö·û´®Îª£º</b><br/>";
echo $str;
echo "<br/>";
echo "<br/>";

$str_rpc = ereg_replace("[0-9]", " ", $str);
echo "<b>Ìæ»»ºó×Ö·û´®Îª£º</b><br/>";
echo $str_rpc;
?>