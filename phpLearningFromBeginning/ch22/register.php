<?php
include_once("include/db_mysql.php");
include_once("include/common.php");

$conn = db_connect($h,$p,$u,$db);

$user_name = $_POST['username'];
$passwd = $_POST['passwd'];
$passwd1 = $_POST['passwd1'];
$email = $_POST['email'];
$come_from = $_POST['from'];

if(empty($user_name) || empty($passwd) || empty($passwd1) || empty($email) || empty($come_from))
{
    $err_info = '注册中的每一项都必须填写或选择！';
    showerrpage($err_info);
    exit;
}

if($passwd != $passwd1)
{
    $err_info = '两次填写的密码不一致！';
    showerrpage($err_info);
    exit;
}
$pwd = md5($passwd);

$sql = "select user_id from users where user_name='".mysql_escape_string($user_name)."'";
$result = mysql_query($sql) or die ('ERROR: '.mysql_error());
if(mysql_num_rows($result)>0)
{
    $err_info = '该用户名已经存在，请更换！';
    showerrpage($err_info);
    exit;
}

$reg_ip = $_SERVER["REMOTE_ADDR"]; 
$sql = "insert into users set user_name='".mysql_escape_string($user_name)."',passwd='".mysql_escape_string($pwd)."',email='".mysql_escape_string($email)."',reg_ip='".$reg_ip."',reg_time=NOW(),come_from='".$come_from."'";
mysql_query($sql) or die ('ERROR: '.mysql_error());

mysql_free_result($result);
mysql_close();

header("location: index.php");    //注册成功将跳转到论坛首页
?>