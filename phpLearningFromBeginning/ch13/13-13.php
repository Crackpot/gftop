<?php
if(!isset($_GET['id']))
{
    echo '参数错误！';
    exit;
}

$id = $_GET['id'];
if(empty($id))
{
    echo '用户ID不能为空！';
    exit;
}

$host = 'localhost';
$user_name = 'root';
$password = 'admin';

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('数据库连接失败：'.mysql_error());
}
mysql_select_db('test');

//先判断是否存在该ID的用户
$sql = "select * from users where id=$id";
$result = mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>SQL：".$sql);
if(!mysql_num_rows($result))
{
    echo '用户ID错误！';
    exit;
}

//删除用户数据
$sql = "delete from users where id=$id";
mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>SQL：".$sql);
mysql_close($conn);

echo '数据删除成功，返回<a href="13-12.php">13-12.php</a>查看数据';
?>