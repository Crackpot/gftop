<?php
$cellphone_brand = array(
'nokia',
'moto',
'lenovo',
'tcl'
);

echo 'ԭ���飺';
echo '<br/>';

echo '<pre>';
print_r($cellphone_brand);
echo '</pre>';

$cpb = array_reverse($cellphone_brand);

echo '<br/>';
echo '��ԭ˳����';
echo '<pre>';
print_r($cpb);
echo '</pre>';
?>
