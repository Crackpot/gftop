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
echo '<br/>';

shuffle($cellphone_brand);
echo '<br/>';

echo 'Ԫ�ر����������';
echo '<br/>';
echo '<br/>';

foreach ($cellphone_brand as $cpb)
echo $cpb.'  ';
echo '<br/>';
?>

