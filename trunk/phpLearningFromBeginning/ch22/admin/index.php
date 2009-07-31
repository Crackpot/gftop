<?php
session_start();
if(isset($_POST['aduser']) && isset($_POST['passwd']))
{
    $user = $_POST['aduser'];
    $passwd = $_POST['passwd'];
    
    if(empty($user) && empty($passwod))
    {
        echo '<p><font color="red">登录用户名或密码错误</font></p>';
        exit;
    }
    mysql_connect("localhost","root","admin");
    mysql_select_db("mybbs") or die("Can't select database");
    
    $passwd = md5($passwd);
    $sql = "select id from admins where name='$user' and passwd='$passwd'";
    $result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
    if($num = mysql_num_rows($result))
    {
        $_SESSION['ad']=$user;
        header("location: main.php");     //如果登录成功，跳转进入后台管理界面首页main.htm
    }
    else
    {
        echo '<p><font color="red">登录用户名或密码错误</font></p>';
        exit;
    }
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>论坛管理系统</title>
<style type="text/css">
<!--
.STYLE1 {font-size: 12px}
.STYLE2 {
    font-size: 18px;
    font-style: italic;
    color: #EC5A1C;
    font-weight: bold;
}
-->
</style>
</head>

<body>

<div align="center">
<form id="form1" name="form1" method="post" action="">
    <p class="STYLE2">论坛后台管理系统</p>
    <table width="291" height="80" border="0" cellpadding="0" cellspacing="1" bgcolor="#1D26E4">
        <tr>
        <td width="83" height="23" bgcolor="#D4D4D4"><div align="right" class="STYLE1">用户名：</div></td>
        <td width="192" bgcolor="#FFFFFF">
            <label><input name="aduser" type="text" id="aduser" /></label>
        </td>
        </tr>
        <tr>
        <td height="22" bgcolor="#D4D4D4"><div align="right" class="STYLE1">密码 ： </div></td>
        <td bgcolor="#FFFFFF">
            <label><input name="passwd" type="password" id="passwd" /></label>
        </td>
        </tr>
        <tr>
        <td colspan="2" bgcolor="#FFFFFF">
            <label><input type="submit" name="Submit" value="提交" /></label>
        </td>
        </tr>
    </table>
</form>
</div>

</body>
</html>