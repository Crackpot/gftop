<?php
$arr1 = array(
0=>100,
"gold"=>"money"
);

$arr2 = array(
'Sunday',
'Saturday',
'Monday',
'Sunday',
'Sunday'
);

echo '<pre>';
echo '����arr1��ȫ�������ǣ�';
print_r(array_keys($arr1));

echo '����arr2��Ԫ�ء�Sunday��ȫ�������ǣ�';
echo '<br/>';
print_r(array_keys($arr2,'Sunday'));
?>