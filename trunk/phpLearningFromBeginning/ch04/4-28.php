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
echo '数组arr1的全部索引是：';
print_r(array_keys($arr1));

echo '数组arr2中元素”Sunday“全部索引是：';
echo '<br/>';
print_r(array_keys($arr2,'Sunday'));
?>
