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
    echo "�ַ���'$str'����";
    if (preg_match($patt_url, $str))
    {
        echo "<b>�Ϸ���URL��ʽ</b>";
        echo "<br>";
        echo "<br>";
    }
    else
    {
        echo "���Ϸ���URL��ʽ";
        echo "<br>";
        echo "<br>";
    }
}
?>