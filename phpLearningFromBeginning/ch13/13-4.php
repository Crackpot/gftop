<?php
$host = 'localhost';
$user_name = 'root';
$password = 'admin';

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('���ݿ�����ʧ�ܣ�'.mysql_error());
}
mysql_select_db('test');

$sql = 'select id,name,city,gender from users';

//����ʹ��mysql_error()��ȡSQL���ִ�г���ʱ�������Ϣ
$result = mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/><br/><br/>���������SQL<br/>".$sql);

if($result)
{
    echo 'SQL��䣺' . $sql . '<br/>�Ѿ��ɹ�ִ�У�';
}

mysql_close($conn);
?>