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

$sql = 'select id,name,city from users';
$result = mysql_query($sql);

if($result)
{
    echo 'SQL��䣺' . $sql . '<br/>�Ѿ��ɹ�ִ�У�';
    $num = mysql_num_rows($result);    //���ú���mysql_num_row()���SELECT����ѯ���������
    echo '<br/>��SQL����ѯ��<b>'.$num.'</b>������';
}

mysql_close($conn);
?>