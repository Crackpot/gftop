<?php
if(!isset($_GET['id']))
{
    echo '��������';
    exit;
}

$id = $_GET['id'];
if(empty($id))
{
    echo '�û�ID����Ϊ�գ�';
    exit;
}

$host = 'localhost';
$user_name = 'root';
$password = 'admin';

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('���ݿ�����ʧ�ܣ�'.mysql_error());
}
mysql_select_db('test');

//���ж��Ƿ���ڸ�ID���û�
$sql = "select * from users where id=$id";
$result = mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>SQL��".$sql);
if(!mysql_num_rows($result))
{
    echo '�û�ID����';
    exit;
}

//ɾ���û�����
$sql = "delete from users where id=$id";
mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>SQL��".$sql);
mysql_close($conn);

echo '����ɾ���ɹ�������<a href="13-12.php">13-12.php</a>�鿴����';
?>