<?php
include_once("include/db_mysql.php");
include_once("include/common.php");
$conn = db_connect($h,$p,$u,$db);

$bid = $_GET['bid'];
$tid = $_GET['tid'];
if(!is_numeric($bid) || !is_numeric($tid))
{
    $error = $ERR['NO_PARAM'];
    showerrpage($error);
    exit;
}

$show_info = "";
$sql = "select board_name,content,DATE_FORMAT(post_time,'%Y-%m-%d %H:%i') ";
$sql .= "as post_time from topics,boards where bid=boards.id and bid=$bid and topics.id=$tid";
$result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
if($num = mysql_num_rows($result))
{
    $row = mysql_fetch_array($result);
    $board_name = $row['board_name'];
    $content = $row['content'];
    $content = str_replace("<br>&nbsp;&nbsp;&nbsp;&nbsp;","\r\n",$content);
    $post_time = $row['post_time'];
}
else
{
    $error = $ERR['NO_PARAM'];
    showerrpage($error);
    exit;
}
$html_title = $HTML_TITLE['mod'];
$board_name_list = getBoardList();
$user_rank_list = userRank($bid);
close_db($conn);

include_once("template/mod_topic.htm");
?>