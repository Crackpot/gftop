<?php
$url_encode = "http%3A%2F%2Flocalhost.com%2F%3Fuser%3Dabcd%26code%3D1234";
$url_str = urldecode($url_encode);

echo "解码前，URL为：<br/>".$url_encode."<br/>";
echo "<br/>";
echo "<hr>";
echo "<br/>";

echo "解码后，URL为：<br/>".$url_str;
?>
