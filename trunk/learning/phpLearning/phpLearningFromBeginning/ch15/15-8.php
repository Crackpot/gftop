<?php
$test_preg = array(
"AK47",
"163.com",
"happy new year!",
"EX0000",
"007 in USA",
"abc123",
"TEST-abc-315",
"123654789",
"Euapa00!"
);

echo "<b>ԭ���飺</b>";
echo "<pre>";
print_r($test_preg);
echo "</pre>";

$preg_arr = preg_grep("/^[A-Z].*[0-9]$/",$test_preg);
echo "<br>";
echo "<b>��ԭ�������������д��ĸ��ͷ�ġ��м�������ַ�����������ֽ�β���ַ����ҳ���</b>";
echo "<pre>";
print_r($preg_arr);
echo "</pre>";
?>