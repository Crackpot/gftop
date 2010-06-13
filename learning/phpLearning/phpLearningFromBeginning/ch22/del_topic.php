<?php
include_once("include/db_mysql.php");
include_once("include/common.php");
session_start();
$conn = db_connect($h,$p,$u,$db);

if(isset($_GET['tid']))
    $tid = $_GET['tid'];
else
    $tid = "";

if(isset($_GET['bid']))
    $bid = $_GET['bid'];
else
    $bid = "";

if(empty($tid) || !is_numeric($tid) || empty($bid) || !is_numeric($bid))
{
    $error = $ERR['NO_PARAM'];
    showerrpage($error);
    exit;
}

if(isset($_SESSION['user_id']))
    $user_id = $_SESSION['user_id'];
else
    $user_id = '';
if(empty($user_id))                  //判断用户是否登录
{
    $error = $ERR['NOT_LOGIN'];
    showerrpage($error);
    exit;
}

$sql = "select user_id from topics where id=".$tid;
$result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
if($num = mysql_num_rows($result))
{
    $row = mysql_fetch_array($result);
    $uid = $row['user_id'];
    
    if($uid != $user_id)             //判断该登录用户是否是该帖的发表用户
    {
        $error = $ERR['OP_ILLEGAL'];
        showerrpage($error);
        exit;
    }
    
    $sql = "delete from topics where id=".$tid;
     mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
}
else
{
    $error = $ERR['NO_PARAM'];
    showerrpage($error);
    exit;
}

close_db($conn);
header("location: list.php?bid=$bid");
?>
