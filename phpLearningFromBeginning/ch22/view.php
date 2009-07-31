<?php
include_once("include/db_mysql.php");
include_once("include/common.php");
session_start();
$conn = db_connect($h,$p,$u,$db);

$str_login = (empty($_SESSION['user_id'])) ? $FUNC['login2'] : "欢迎你，".$_SESSION['user_name']."！ <a href=\"logout.php\">注销退出</a>";
$str_notlogin = (empty($_SESSION['user_id'])) ? $FUNC['notlogin'] : "";

$bid = $_GET['bid'];
$tid = $_GET['tid'];
if(!is_numeric($bid) || !is_numeric($tid))
{
    $error = $ERR['NO_PARAM'];
    showerrpage($error);
    exit;
}

if(isset($_SESSION['user_id']))
    $user_id = $_SESSION['user_id'];
else
    $user_id = '';

$sql = "select board_name from boards where id=$bid";
$result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
if($num = mysql_num_rows($result))
{
    $row = mysql_fetch_array($result);
    $board_name = $row['board_name'];
    
    $sql = "select t.id,t.fid,u.user_name,u.user_id as user_id,content,DATE_FORMAT(post_time,'%Y-%m-%d %H:%i') ";
    $sql .= "as post_time from topics t,users u ";
    $sql .= "where bid=".$bid." and fid=0 and id=$tid and t.user_id=u.user_id order by id desc";
    
    $result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
    if($num = mysql_num_rows($result))
    {
        $topic_list = "<div><ul>";
        while($row = mysql_fetch_array($result))
        {
            $tid = $row['id'];
            $topic_list .= "<hr noshade size=\"1\" color=\"silver\" align=\"center\" width=\"100%\">";
            $topic_list .= "<li><a href=\"userinfo.php?uid=".$row['user_id']."\">".$row['user_name']."</a>";
            $topic_list .= "&nbsp;&nbsp;&nbsp;<font class=\"post_time\">".$row['post_time']."</font>";
            $str_mod = ($user_id == $row['user_id']) ? "<a href=\"mod_topic.php?bid=$bid&tid=$tid\">".$FUNC['modify']."</a>&nbsp;&nbsp;<a href=\"del_topic.php?bid=$bid&tid=$tid\">".$FUNC['delete']."</a>" : '';
            $topic_list .= "<span style='position:absolute;left:50%;'> ".$str_mod."</span>";
            $topic_list .= "<br/>&nbsp;&nbsp;&nbsp;&nbsp;".$row['content']."</li>";
            $topic_list .= getReplyPost($tid);
        }
        $topic_list .= "</ul></div>";
    }
    else
    {
        $topic_list = $ERR['TOPIC_NOT_EXIST'];
    }
}
else
{

    $error = $ERR['BOARD_NOT_EXIST'];
    showerrpage($error);
    exit;
}

$html_title = $HTML_TITLE['view'];
$board_name_list = getBoardList();
$user_rank_list = userRank($bid);

close_db($conn);
include_once("template/view.htm");
?>