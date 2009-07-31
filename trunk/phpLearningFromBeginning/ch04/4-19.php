<?php
$arr = array(
'Beijing',
'Lodon',
'Rome'
);

echo '原数组：';
echo '<pre>';
print_r($arr);

array_push($arr,'Oslo','Seoul');
echo '<br/>';
echo '<br/>';

echo '调用函数array_push()之后：';
echo '<br/>';
print_r($arr);
?>
