<?php
$host = 'localhost';
$user_name = 'root';
$password = 'admin';

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('数据库连接失败：'.mysql_error());
}
mysql_select_db('test');

$sql = 'select id,name,city,created_time from users';

$result = mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>产生问题的SQL：".$sql);
?>
<html>
<head>
<title>13-12.php</title>
<script language="javascript">

</script>
</head>
<center>

<body>
<table width="75%" border="0" cellpadding="0" cellspacing="1" bgcolor="#7B7B84">
    <tr bgcolor="#8BBCC7"> 
        <td height="33"><div align="center"><strong>用户ID</strong></div></td>
        <td><div align="center"><strong>用户名称</strong></div></td>
        <td><div align="center"><strong>来自城市</strong></div></td>
        <td><div align="center"><strong>注册时间</strong></div></td>
        <td><div align="center"><strong>操作</strong></div></td>
    </tr>

<?php
if($num = mysql_num_rows($result))
{
    while($row = mysql_fetch_array($result,MYSQL_ASSOC))
    {
?>
    <tr bgcolor="#FFFFFF"> 
        <td height="22" align="right"><?php echo $row['id']; ?>&nbsp;</td>
        <td height="22">&nbsp;<?php echo $row['name']; ?>&nbsp;</td>
        <td height="22">&nbsp;<?php echo $row['city']; ?>&nbsp;</td>
        <td height="22">&nbsp;<?php echo $row['created_time']; ?>&nbsp;</td>
        <td height="22">&nbsp;<a onclick="javascript:if(confirm('确定要删除用户信息吗?')) return true; else return false;" href="13-13.php?id=<?php echo $row['id']; ?>">删除</a>&nbsp;</td>
    </tr>
<?php
    }
}
mysql_close($conn);
?>

</table>
</body>
</center>
</html>