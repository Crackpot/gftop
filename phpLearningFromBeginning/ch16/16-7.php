<?php
set_error_handler('myHandler');     //�Զ����������

function myHandler($code, $msg, $file, $line)
{
    echo "<br/>";
    echo "���� <b>$file</b> ִ�й����У��ڵ� <b>$line</b> �У�����һ������";
    echo "<br/>";
    echo "�������Ϊ��<b>$code</b>, �����ԭ����: <b>$msg</b>";
}

echo $uvar;
?>
