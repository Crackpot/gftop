<?php
$url = "http://localhost.com/?user=abcd&code=1234";
$decode_url = urlencode($url);

echo "编码前，URL为：<br/>".$url."<br/>";
echo "<br/>";
echo "<hr>";
echo "<br/>";

echo "编码后，URL为：<br/>".$decode_url;
?>
