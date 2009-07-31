<?php
$cellphone_brand = array(
'nokia',
'moto',
'lenovo',
'tcl'
);

echo '原数组：';
echo '<br/>';

echo '<pre>';
print_r($cellphone_brand);
echo '</pre>';

$cpb = array_reverse($cellphone_brand);

echo '<br/>';
echo '按原顺序反向：';
echo '<pre>';
print_r($cpb);
echo '</pre>';
?>
