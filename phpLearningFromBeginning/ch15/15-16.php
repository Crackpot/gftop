<?php
$str_arr = array(
"mymail@somesite.com",
"my_mail@somesite.com",
"my-mail@somesite.com",
"my.mail@site.com.cn",
"mymail@site.com.ccoomm",
"mymail@site.cn",
"mymail@@@lsite.com",
"mymail@site",
"MyMail@somesite.com",
"My2007@somesite.com",
"163mail_for-me777@somesite.com",
);

$patt_email = "/^[_a-zA-Z0-9-]+@([0-9a-z][0-9a-z-]+\.)+[a-z]{2,4}$/";

foreach ($str_arr as $str)
{
    echo "�ַ���'$str'����";
    if (preg_match($patt_email, $str))
    {
        echo "<b>�Ϸ���Email��ʽ</b>";
        echo "<br>";
        echo "<br>";
    }
    else
    {
        echo "���Ϸ���Email��ʽ";
        echo "<br>";
        echo "<br>";
    }
}
?>