<?php
$host = 'localhost';
$user_name = 'root';
$password = 'admin';

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('���ݿ�����ʧ�ܣ�'.mysql_error());
}
echo '���ݿ����ӳɹ���';

if(mysql_close($conn))
{
    echo '<br/>........<br/>';
    echo '�����ݿ�������Ѿ��ɹ��ر�';
}
?>