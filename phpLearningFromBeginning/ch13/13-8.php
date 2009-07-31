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

if(isset($_GET['page']))     //由GET方法获得页面传入当前页数的参数
{
    $page = $_GET['page'];
}
else
{
    $page = 1;
}
$page_size = 2;              //每页显示两条数据

//获取数据总量
$sql = 'select * from users';
$result = mysql_query($sql);
$total = mysql_num_rows($result);

//开始计算总页数
if($total)
{
    //如果总数据量小于$page_size，那么只有一页
    if($total < $page_size)
        $page_count = 1;
    //如果有余数，则总页数等于总记录数除以页数的结果取整再加1
    if($total % $page_size)
    {
        $page_count = (int)($total/$page_size) + 1;
    }
    //如果没有余数，则页数等于总数据量除以每页数的结果
    else
    {
        $page_count = $total/$page_size;
    }
}
else
{
    $page_count = 0;
}
//翻页链接
$turn_page = '';
if($page == 1)
{
    $turn_page .= '首页 | 上一页 |';
}
else
{
    $turn_page .= '<a href=13-8.php?page=1> 首页</a> | <a href=13-8.php?page='.($page-1).'> 上一页 </a> |';
}
if($page == $page_count || $page_count == 0)
{
    $turn_page .= ' 下一页 | 尾页';
}
else
{
    $turn_page .= '<a href=13-8.php?page='.($page+1).'> 下一页 </a>|<a href=13-8.php?page='.$page_count.'> 尾页 </a>';
}

$sql = 'select id,name,city,created_time from users limit '. ($page-1)*$page_size .', '.$page_size;
$result = mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>产生问题的SQL：".$sql);
?>
<html>
<head>
<title>13-8.php</title>
</head>
<center>

<body>
<table width="75%" border="0" cellpadding="0" cellspacing="1" bgcolor="#7B7B84">
    <tr bgcolor="#8BBCC7"> 
        <td height="33"><div align="center"><strong>用户ID</strong></div></td>
        <td><div align="center"><strong>用户名称</strong></div></td>
        <td><div align="center"><strong>来自城市</strong></div></td>
        <td><div align="center"><strong>注册时间</strong></div></td>
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
    </tr>
<?php
    }
}
echo $turn_page.'<br/><br/>';
mysql_close($conn);
?>

</table>
</body>
</center>
</html>