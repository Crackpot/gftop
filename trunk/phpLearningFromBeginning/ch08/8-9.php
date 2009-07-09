<?php
//设置多个cookie，存放在数组mycookie中
setcookie("mycookie['three']", "cookiethree");
setcookie("mycookie['two']", "cookietwo");
setcookie("mycookie['one']", "cookieone");

//刷新页面后，将所有cookie显示出来
if(isset($_COOKIE['mycookie']))
{
    foreach ($_COOKIE['mycookie'] as $name => $value)
    {
        echo "$name : $value <br />\n";
    }
}
?>