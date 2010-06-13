<?php
$str_arr = array(
"http://www.myoosite.com",
"www.myoosite.com",
"http://www.myoosite.com/abc/123.html",
"//myoosite.com",
":www.myoosite.com"
);

$patt_url = "/^(http:\/\/)?[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*.+$/";

foreach ($str_arr as $str)
{
    echo "字符串'$str'：是";
    if (preg_match($patt_url, $str))
    {
        echo "<b>合法的URL格式</b>";
        echo "<br>";
        echo "<br>";
    }
    else
    {
        echo "不合法的URL格式";
        echo "<br>";
        echo "<br>";
    }
}
?>