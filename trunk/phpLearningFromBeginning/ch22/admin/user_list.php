<?php
if(isset($_GET['o']))
    $op = $_GET['o'];
else
    $op = '';
if($op=='r')                 //按用户ID排序
{
    $tmp_sql = "order by user_id desc";
}
elseif($op == 'l')           //按登录时间排序
{
    $tmp_sql = "order by login_time desc";
}
else
    $tmp_sql = "";

$info = "<a href=\"user_list.php\" style=\"font-size: 13px;\">列出所有</a> ";
$info .="<a href=\"?o=r\" style=\"font-size: 13px;\">按最新注册排列</a>    ";
$info .= "<a href=\"?o=l\" style=\"font-size: 13px;\">按最近登录排列</a><br/><br/>";
$info .= "<table border=1 style=\"font-size: 13px;\"><tr bgcolor=\"#abcdef\" align=\"center\">";
$info .= "<td><b>用户ID</b></td><td><b>用户名</b></td><td><b>Email</b></td><td><b>注册时间</b></td>";
$info .= "<td><b>注册IP</b></td><td><b>登录时间</b></td><td><b>登录IP</b></td><td><b>操作</b></td></tr>";

mysql_connect("localhost","root","admin");
mysql_select_db("mybbs") or die("Can't select database");

if(!empty($_GET['del']))     //删除用户的操作
{
    $user_id = $_GET['del'];
    $sql = "delete from users where user_id=".$user_id;
    mysql_query($sql) or die ('ERROR: '.mysql_error());
}

$sql = "select user_id,user_name,email,reg_ip,reg_time,login_ip,login_time from users ".$tmp_sql;
$result = mysql_query($sql) or die ('ERROR: '.mysql_error());
if(mysql_num_rows($result))
{
    while($row = mysql_fetch_array($result))
    {
        if(empty($row['email']))
            $email = "未填写";
        else
            $email = $row['email'];
        $info .= "<tr><td>".$row['user_id']."</td><td>".$row['user_name']."</td><td>".$email;
        $info .= "</td><td>".$row['reg_time']."</td><td>".$row['reg_ip'];
        $info .= "</td><td>".$row['login_time']."</td><td>";
        $info .= $row['login_ip']."</td><td><a href=\"?del=".$row['user_id']."\">删除</a></td><tr>";
    }
    $info .= "</table>";
}
else
{
    $info = "暂无注册用户信息";
}
echo $info;
?>