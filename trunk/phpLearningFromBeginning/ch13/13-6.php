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

$result = mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>���������SQL��".$sql);

if($num = mysql_num_rows($result))
{
    echo '<pre>';
    while($row = mysql_fetch_array($result,MYSQL_ASSOC))
    {
        print_r($row);
    }
}

mysql_close($conn);
?>