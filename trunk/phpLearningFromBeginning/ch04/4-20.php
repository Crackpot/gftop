<?php
$arr = array(
'Beijing',
'Lodon',
'Rome',
'Moscow',
'Singapore'
);

echo '原数组：';
echo '<pre>';
print_r($arr);
echo '</pre>';

$arr_tmp = array_pop($arr);
echo '<br/>';

echo '<pre>';
echo 'pop出数组的元素是：<b>'.$arr_tmp .'</b>';
echo '<br/>';

echo '调用函数array_pop()之后：';
print_r($arr);
?>