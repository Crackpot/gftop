<?php
$host = 'localhost';
$user_name = 'root';
$password = 'admin';
$arr_city = array('Beijing'=>'北京','NewYork'=>'纽约','Paris'=>'巴黎','London'=>'伦敦','Rome'=>'罗马');

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('数据库连接失败：'.mysql_error());
}
mysql_select_db('test');

if(!isset($_GET['uid']))
{
    echo '参数错误！';
    exit;
}
$id = $_GET['uid'];

$sql = "select * from users where id=$id";
$result = mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>SQL：".$sql);
if(!mysql_num_rows($result))
{
    echo '用户ID错误！';
    exit;
}

$row = mysql_fetch_array($result);

$name = $_POST['user_name'];
$city = $_POST['city'];
if(!empty($name) || trim($name)!='')
{
    $sql = "update users set name='" . $name . "',city='" . $city . "' where id=$id";
    mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>SQL：".$sql);
    mysql_close($conn);

    echo '数据修改成功，打开<a href="13-7.php">13-7.php</a>查看数据';
    exit;
}
?>

<html>
<head>
<title>13-11.php</title>
</head>

<body>
<b>修改用户信息</b>
<form name="form" method="post" action="13-11.php?uid=<?php echo $id; ?>">
    <table width="75%" border="0" cellpadding="0" cellspacing="2">
        <tr> 
            <td width="24%" height="29">用户名：</td>
            <td width="76%"><input name="user_name" type="text" id="user_name" size="20" value="<?php echo $row['name']; ?>"></td>
        </tr>
        <tr> 
        <td height="25">来自城市：</td>
        <td>
        <select name="city">
        <?php
        foreach($arr_city as $k=>$v)
        {
            $option = ($row['city'] == $k) ? '<option value="'.$k.'" selected>'.$v.'</option>' : '<option value="'.$k.'">'.$v.'</option>';
            echo $option.'\n';
        }    
        ?>
        </select>
        </td>
        </tr>
        <tr>
        <td>注册时间：</td>
        <td><?php echo $row['created_time']; ?></td>
        </tr>
        <tr> 
            <td height="31">
            <input type="submit" name="Submit" value="修改"></td>
            <td>&nbsp;</td>
        </tr>
    </table>
</form>
</body>
</html>