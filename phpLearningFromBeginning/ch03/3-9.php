<?php
session_start();

$user = $_POST['user_name'];
if(!empty($user))
{
    $_SESSION['user'] = $user;
    $welcome = "���ã�".$user."����¼��������Ϣ���ύ��<br/>";
}
?>
<html>
<head>
<title>3-9.php �û���Ϣ¼��</title>
</head>

<body>
<?php
    echo $welcome;
?>
<form name="info" action="" method="POST">
<table border="0">
    <tr><td>�Ա�</td><td><input name="gender" type="radio" value="��">�� <input name="gender" type="radio" value="Ů">Ů</td></tr>
    <tr><td>���䣺</td><td><input name="age" type="input" size="3"></td></tr>
    <tr>
        <td>Ѫ�ͣ�</td>
        <td>
            <select name="blood_type">
            <option value="A">A��</option>
            <option value="B">B��</option>
            <option value="O">O��</option>
            <option value="AB">AB��</option>
            <option value="����">����Ѫ��</option>
            </select>
        </td>
    </tr>
    <tr><td><input type="submit" value="�ύ"></td></tr>
</table>
</form>

</body>
</html>