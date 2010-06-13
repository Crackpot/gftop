<?php
$host = 'localhost';
$user_name = 'root';
$password = 'admin';

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('数据库连接失败：<br/>'.mysql_error());
}
echo '数据库连接成功！';
?>