<?php
$url = "http://www.somesite.com:8000/php/code?id=100&cid=900";
$ret_arr = parse_url($url);

echo "Ҫ�����ĵ�ַ��<br/>".$url;
echo "<hr>";

echo "<pre>";
echo "����������£�<br/>";
print_r($ret_arr);
?>
