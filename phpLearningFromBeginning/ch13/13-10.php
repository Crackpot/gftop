<?php
$host = 'localhost';
$user_name = 'root';
$password = 'admin';

$name = $_POST['user_name'];
$city = $_POST['city'];

if(empty($name) || trim($name)=='')
{
    echo '����д�û�����<a href="13-9.html">����</a>';
    exit;
}

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('���ݿ�����ʧ�ܣ�'.mysql_error());
}
mysql_select_db('test');

$sql = "insert into users set id=7,name='" . $name . "',city='" . $city . "',created_time=NOW()";
mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>SQL��".$sql);
mysql_close($conn);

echo '���ݲ���ɹ�����<a href="13-7.php">13-7.php</a>�鿴����';
?>