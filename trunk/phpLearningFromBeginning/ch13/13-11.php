<?php
$host = 'localhost';
$user_name = 'root';
$password = 'admin';
$arr_city = array('Beijing'=>'����','NewYork'=>'ŦԼ','Paris'=>'����','London'=>'�׶�','Rome'=>'����');

$conn = mysql_connect($host,$user_name,$password);
if(!$conn)
{
    die('���ݿ�����ʧ�ܣ�'.mysql_error());
}
mysql_select_db('test');

if(!isset($_GET['uid']))
{
    echo '��������';
    exit;
}
$id = $_GET['uid'];

$sql = "select * from users where id=$id";
$result = mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>SQL��".$sql);
if(!mysql_num_rows($result))
{
    echo '�û�ID����';
    exit;
}

$row = mysql_fetch_array($result);

$name = $_POST['user_name'];
$city = $_POST['city'];
if(!empty($name) || trim($name)!='')
{
    $sql = "update users set name='" . $name . "',city='" . $city . "' where id=$id";
    mysql_query($sql) OR die("<br/>ERROR: <b>".mysql_error()."</b><br/>SQL��".$sql);
    mysql_close($conn);

    echo '�����޸ĳɹ�����<a href="13-7.php">13-7.php</a>�鿴����';
    exit;
}
?>

<html>
<head>
<title>13-11.php</title>
</head>

<body>
<b>�޸��û���Ϣ</b>
<form name="form" method="post" action="13-11.php?uid=<?php echo $id; ?>">
    <table width="75%" border="0" cellpadding="0" cellspacing="2">
        <tr> 
            <td width="24%" height="29">�û�����</td>
            <td width="76%"><input name="user_name" type="text" id="user_name" size="20" value="<?php echo $row['name']; ?>"></td>
        </tr>
        <tr> 
        <td height="25">���Գ��У�</td>
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
        <td>ע��ʱ�䣺</td>
        <td><?php echo $row['created_time']; ?></td>
        </tr>
        <tr> 
            <td height="31">
            <input type="submit" name="Submit" value="�޸�"></td>
            <td>&nbsp;</td>
        </tr>
    </table>
</form>
</body>
</html>