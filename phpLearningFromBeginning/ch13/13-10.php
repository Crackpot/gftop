<?php
$host = 'localhost';
$user_name = 'root';
$password = 'admin';

$name = $_POST['user_name'];
$city = $_POST['city'];

if(empty($name) || trim($name)=='')
{
    echo '请填写用户名！<a href="13-9.html">返回</a>';
    exit;
}

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('数据库连接失败：'.mysql_error());
}
mysql_select_db('test');

$sql = "insert into users set id=7,name='" . $name . "',city='" . $city . "',created_time=NOW()";
mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>SQL：".$sql);
mysql_close($conn);

echo '数据插入成功，打开<a href="13-7.php">13-7.php</a>查看数据';
?>