<?php
$host = 'localhost';
$user_name = 'root';
$password = 'admin';

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('���ݿ�����ʧ�ܣ�'.mysql_error());
}
mysql_select_db('test');

if(isset($_GET['page']))     //��GET�������ҳ�洫�뵱ǰҳ���Ĳ���
{
    $page = $_GET['page'];
}
else
{
    $page = 1;
}
$page_size = 2;              //ÿҳ��ʾ��������

//��ȡ��������
$sql = 'select * from users';
$result = mysql_query($sql);
$total = mysql_num_rows($result);

//��ʼ������ҳ��
if($total)
{
    //�����������С��$page_size����ôֻ��һҳ
    if($total < $page_size)
        $page_count = 1;
    //���������������ҳ�������ܼ�¼������ҳ���Ľ��ȡ���ټ�1
    if($total % $page_size)
    {
        $page_count = (int)($total/$page_size) + 1;
    }
    //���û����������ҳ������������������ÿҳ���Ľ��
    else
    {
        $page_count = $total/$page_size;
    }
}
else
{
    $page_count = 0;
}
//��ҳ����
$turn_page = '';
if($page == 1)
{
    $turn_page .= '��ҳ | ��һҳ |';
}
else
{
    $turn_page .= '<a href=13-8.php?page=1> ��ҳ</a> | <a href=13-8.php?page='.($page-1).'> ��һҳ </a> |';
}
if($page == $page_count || $page_count == 0)
{
    $turn_page .= ' ��һҳ | βҳ';
}
else
{
    $turn_page .= '<a href=13-8.php?page='.($page+1).'> ��һҳ </a>|<a href=13-8.php?page='.$page_count.'> βҳ </a>';
}

$sql = 'select id,name,city,created_time from users limit '. ($page-1)*$page_size .', '.$page_size;
$result = mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>���������SQL��".$sql);
?>
<html>
<head>
<title>13-8.php</title>
</head>
<center>

<body>
<table width="75%" border="0" cellpadding="0" cellspacing="1" bgcolor="#7B7B84">
    <tr bgcolor="#8BBCC7"> 
        <td height="33"><div align="center"><strong>�û�ID</strong></div></td>
        <td><div align="center"><strong>�û�����</strong></div></td>
        <td><div align="center"><strong>���Գ���</strong></div></td>
        <td><div align="center"><strong>ע��ʱ��</strong></div></td>
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