<?php
include_once("include/db_mysql.php");
include_once("include/common.php");
session_start();
$conn = db_connect($h,$p,$u,$db);

if(isset($_POST['username']) && isset($_POST['passwd']))
{
    $user_name = $_POST['username'];
    $passwd = $_POST['passwd'];
    
    if(!empty($user_name) && !empty($passwd))
    {
        $pw = md5($passwd);
        $sql = "select user_id from users where user_name='".mysql_escape_string($user_name)."' and passwd='".mysql_escape_string($pw)."'";
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
            
            header("location: index.php");
        }
        else
        {
            $error = $ERR['INVALID_USER'];
            showerrpage($error);
            exit;
        }
    }
}
?>
<html>
<head><title>论坛用户注册</title>
<style type="text/css">
<!--
.STYLE2 {
    font-size: 12px;
    font-weight: bold;
}
.STYLE3 {font-size: 12px}
-->
</style>
</head>
<body>
<form id="form" name="form" method="post" action="">
  <table width="329" border="0" align="center" cellpadding="0" cellspacing="1" bgcolor="#F5A510">
    <tr>
      <td height="30" colspan="2" bgcolor="#FEFBE0"><div align="center"><span class="STYLE2">用户登录</span></div></td>
    </tr>
    <tr>
      <td width="100" height="33" bgcolor="#F2F3F4"><div align="right" class="STYLE3">用户名：</div></td>
      <td width="213" bgcolor="#F2F3F4">&nbsp;<input type="text" name="username" /></td>
    </tr>
    <tr>
      <td height="36" bgcolor="#F2F3F4"><div align="right" class="STYLE3">密码：</div></td>
      <td bgcolor="#F2F3F4"><label>
        &nbsp;<input type="password" name="passwd" />
      </label></td>
    </tr>
    <tr>
      <td height="36" colspan="2" bgcolor="#F2F3F4"><label>
        &nbsp;<input type="submit" name="Submit" value="登录" />
      </label></td>
    </tr>
  </table>
</form>
<p>&nbsp;</p>
</body>
</html>