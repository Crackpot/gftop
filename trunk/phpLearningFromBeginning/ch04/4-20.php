<?php
$arr = array(
'Beijing',
'Lodon',
'Rome',
'Moscow',
'Singapore'
);

echo 'ԭ���飺';
echo '<pre>';
print_r($arr);
echo '</pre>';

$arr_tmp = array_pop($arr);
echo '<br/>';

echo '<pre>';
echo 'pop�������Ԫ���ǣ�<b>'.$arr_tmp .'</b>';
echo '<br/>';

echo '���ú���array_pop()֮��';
print_r($arr);
?>