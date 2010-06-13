<?php
$str = "tea,milk,coffee,juice";
$arr = explode(',',$str);
echo "<pre>";
print_r($arr);

$arr = explode(',',$str,2);
print_r($arr);
?>
