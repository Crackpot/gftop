<?php
$url = "http://www.somesite.com:8000/php/code?id=100&cid=900";
$ret_arr = parse_url($url);

echo "要分析的地址：<br/>".$url;
echo "<hr>";

echo "<pre>";
echo "分析结果如下：<br/>";
print_r($ret_arr);
?>
