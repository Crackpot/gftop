<?php
//���ö��cookie�����������mycookie��
setcookie("mycookie['three']", "cookiethree");
setcookie("mycookie['two']", "cookietwo");
setcookie("mycookie['one']", "cookieone");

//ˢ��ҳ��󣬽�����cookie��ʾ����
if(isset($_COOKIE['mycookie']))
{
    foreach ($_COOKIE['mycookie'] as $name => $value)
    {
        echo "$name : $value <br />\n";
    }
}
?>