<?php
include_once("include/db_mysql.php");
include_once("include/common.php");
$conn = db_connect($h,$p,$u,$db);

if(isset($_GET['uid']))
    $uid = $_GET['uid'];
else
    $uid = "";

if(empty($uid) || !is_numeric($uid))
{
    $error = $ERR['USER_NOT_EXIT'];
    showerrpage($error);
    exit;
}

$user_info = "";
$sql = "select user_id,user_name,come_from,DATE_FORMAT(reg_time,'%Y-%m-%d') as reg_time from users where user_id=$uid";
$result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
if($row = mysql_fetch_array($result))
{
    $user_info .= "<table align=\"center\" border=\"0\">";
    $user_info .= "<tr><td colspan=\"2\">====用户信息=====</td></tr>";
    $user_info .= "<tr><td align=\"right\">用户名： </td><td align=\"left\">".$row['user_name']."</td></tr>";
    $user_info .= "<tr><td align=\"right\">来自： </td><td align=\"left\">".$row['come_from']."</td></tr>";
    $user_info .= "<tr><td align=\"right\">注册时间： </td><td align=\"left\">".$row['reg_time']."</td></tr>";
    $user_info .= "</table>";
}

$html_title = $HTML_TITLE['userinfo'];
$board_name_list = getBoardList();

close_db($conn);

include_once("template/userinfo.htm");
?>