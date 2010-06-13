<?php
$arr1 = array(
'a'=>'green',
'b'=>'brown',
'c'=>'blue',
'red',
'p'=>'pink'
);

$arr2 = array(
'a'=>'green',
'yellow',
'red',
'p'=>'pink',
);

$result_array = array_intersect_assoc($arr1, $arr2);

echo '<pre>';
print_r($result_array);
echo '</pre>';
?> 