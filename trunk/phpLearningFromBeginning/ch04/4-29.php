<?php
function cube($n)
{
    $cb = $n*$n*$n;
    return $cb;
}

$a = array(1, 2, 3, 4, 5);
$b = array_map("cube", $a);

echo '����ԭ�����Ԫ�ص�������������£�';
echo '<br/>';
echo '<pre>';

print_r($b);
?>