<?php
$arr1 = array('Earth','Venus');
$arr2 = array(4=>'Mars',5=>'Jupiter',6=>'Saturn');

$planet = array_merge($arr1,$arr2);
echo '<pre>';
print_r($planet);
?>