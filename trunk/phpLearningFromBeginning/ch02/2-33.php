<?php
function say_hello($some_name = "Jack")
{
    echo "Hello,".$some_name;
    echo "<br/>";
    echo "<br/>";
}

say_hello();           //��ʹ���κβ������ú���say_helloʱ��������ʹ�ú��������Ĭ�ϲ�����Jack��
say_hello("Jenny");    //ʹ�ò�����Jenny�����ú���say_hello
say_hello("Harry");
say_hello("Ema");
?>