<?php
include_once("include/db_mysql.php");
include_once("include/common.php");

session_start();
$conn = db_connect($h,$p,$u,$db);

if(isset($_SESSION['user_id']))
    $user_id = $_SESSION['user_id'];

if(empty($user_id))
{
    $user_name = $_POST['username'];
    $passwd = $_POST['passwd'];
    if(!empty($user_name) && !empty($passwd))
    {
        $pw = md5($passwd);
        $sql = "select user_id from users where user_name='".mysql_escape_string($user_name);
        $sql .= "' and passwd='".mysql_escape_string($pw)."'";
        $result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
        if(!mysql_num_rows($result)==0)
        {
            $row = mysql_fetch_array($result);
            $user_id = $row['user_id'];
            $login_ip = $_SERVER["REMOTE_ADDR"]; 
            $sql = "update users set login_ip='".$login_ip."',login_time=NOW() where user_id=".$user_id;
            mysql_query($sql);
            
            $_SESSION['user_id'] = $user_id;
            $_SESSION['user_name'] = $user_name;
        }
        else
        {
            $error = $ERR['INVALID_USER'];
            showerrpage($error);
            exit;
        }
    }
    else
    {
        $error = $ERR['NOT_LOGIN'];
        showerrpage($error);
        exit;
    }
}

$bid = $_POST['bid'];
$content = $_POST['content'];
$fid = $_POST['tid'];         //主题帖id
$action = $_POST['actions'];  //回复帖操作选项，如回复、修改等。

if(empty($content))
{
    $error = $ERR['NONE_CONTENT'];
    showerrpage($error);
    exit;    
}

$content = delete_htm($content);
$content = str_replace("\r\n","<br>&nbsp;&nbsp;&nbsp;&nbsp;",$content);

if($action == "rpl")          //回复帖子的操作选项
{
    if(empty($bid) || empty($fid) || !is_numeric($bid) || !is_numeric($fid))
    {
        $error = $ERR['NO_PARAM'];
        showerrpage($error);
        exit;
    }
    $content = mysql_escape_string($content);
    $sql = "insert into topics (bid,fid,user_id,content,post_time) values($bid,$fid,$user_id,'$content',NOW())";
    $return_url = "view.php?bid=$bid&tid=$fid";
}
elseif($action == "mod")      //修改帖子的操作选项
{
    if(empty($bid) || empty($fid) || !is_numeric($bid) || !is_numeric($fid))
    {
        $error = $ERR['NO_PARAM'];
        showerrpage($error);
        exit;
    }
    $content = mysql_escape_string($content);
    $sql = "update topics set content='".$content."',edit_time=NOW() where bid=$bid and id=$fid";
    $return_url = "view.php?bid=$bid&tid=$fid";
}
else                          //新发帖子
{
    if(empty($bid) || !is_numeric($bid))
    {
        $error = $ERR['NO_PARAM'];
        showerrpage($error);
        exit;
    }
    $content = mysql_escape_string($content);
    $sql = "insert into topics (bid,user_id,content,post_time) values($bid,$user_id,'$content',NOW())";
    $return_url = "list.php?bid=$bid";
}
mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
$pid = mysql_insert_id();

close_db($conn);

header("Location: $return_url");
exit;
?>