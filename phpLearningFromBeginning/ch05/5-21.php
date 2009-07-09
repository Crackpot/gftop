<?php
$str = 'How are you?';
echo 'Ô­×Ö·û´®£º';
echo '<br/>';

echo $str;
echo '<br/>';
echo '<br/>';

$arr1 = str_split($str);
$arr2 = str_split($str, 3);

echo '<pre>';
print_r($arr1);
print_r($arr2);
echo '</pre>';
?>