<?php
$host = 'localhost';
$user_name = 'root';
$password = 'admin';

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('数据库连接失败：'.mysql_error());
}
mysql_select_db('test');

$sql = 'select id,name,city,gender from users';

//这里使用mysql_error()获取SQL语句执行出错时的相关信息
$result = mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/><br/><br/>产生问题的SQL<br/>".$sql);

if($result)
{
    echo 'SQL语句：' . $sql . '<br/>已经成功执行！';
}

mysql_close($conn);
?>