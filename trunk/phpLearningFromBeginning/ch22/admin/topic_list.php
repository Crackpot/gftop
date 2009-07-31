<?php
$info = "====论坛列表====<br/>";
$info .= "<li><a href=\"topic_list.php\">所有帖子</a></li><br>";

mysql_connect("localhost","root","admin");
mysql_select_db("mybbs") or die("Can't select database");

$sql = "select id,board_name from boards";
$result = mysql_query($sql) or die ('ERROR: '.mysql_error());
if(mysql_num_rows($result))
{
    while($row = mysql_fetch_array($result))
    {
        $bid = $row['id'];
        $info .= "<div><li><a href=\"?bid=$bid\">".$row['board_name']."</a></li><br>";
    }
}
else
{
    echo "暂无论坛";
    exit;
}

$info .= "<br><table border=1 style=\"font-size: 13px;\"><tr bgcolor=\"#abcdef\" align=\"center\"><td><b>ID</b></td><td><b>用户名</b></td><td><b>帖子内容</b></td><td><b>操作</b></td></tr>";

//删除帖子及其回复
if(isset($_GET['del']))
{
    $tid = $_GET['del'];
    $sql = "delete from topics where id=$tid or fid=$tid";
    mysql_query($sql) or die ('ERROR: '.mysql_error());
}

if(isset($_GET['bid']))
{
    $bid = $_GET['bid'];
    $tmp_sql = "and bid=$bid";
}
else
{
    $tmp_sql = "";
}

$sql = "select id,bid,fid,users.user_name,content from topics,users where topics.user_id=users.user_id and fid=0 ".$tmp_sql." order by id desc";
$result = mysql_query($sql) or die ('ERROR: '.mysql_error());
if(mysql_num_rows($result))
{
    while($row = mysql_fetch_array($result))
    {
        $info .="<tr><td>".$row['id']."</td><td>".$row['user_name']."</td><td>".$row['content']."</td><td> <a href=\"?del=".$row['id']."\">删除</a></td></tr>";
    }
    $info .= "</table>";
}
else
{
    $info = "暂无帖子信息";
}

mysql_close();
?>

<html>
<head><title>论坛管理</title>
<link href="style.css" rel="stylesheet" type="text/css">
</head>
<body>

<div><?=$info;?></div>

</body>
</html>