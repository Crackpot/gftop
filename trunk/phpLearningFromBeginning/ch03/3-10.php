<?php
session_start();

$user = $_POST['user_name'];
if(!empty($user))
{
    $_SESSION['user'] = $user;
    $welcome = "您好，".$user."！请录入以下信息后提交。<br/>";
}

$gender = $_POST['gender'];
$age = $_POST['age'];
$blood = $_POST['blood_type'];

if(!empty($gender) && !empty($age) && !empty($blood))
{
    echo "性别：".$gender."<br/>";
    echo "年龄：".$age."<br/>";
    echo "血型：".$blood."<br/>";
}
else
{
?>

<html>
<head>
<title>3-9.php 用户信息录入</title>
</head>

<body>
<?php
    echo $welcome;
?>
<form name="info" action="" method="POST">
<table border="0">
    <tr><td>性别：</td><td><input name="gender" type="radio" value="男">男 <input name="gender" type="radio" value="女">女</td></tr>
    <tr><td>年龄：</td><td><input name="age" type="input" size="3"></td></tr>
    <tr>
        <td>血型：</td>
        <td>
            <select name="blood_type">
            <option value="A">A型</option>
            <option value="B">B型</option>
            <option value="O">O型</option>
            <option value="AB">AB型</option>
            <option value="其他">其他血型</option>
            </select>
        </td>
    </tr>
    <tr><td><input type="submit" value="提交"></td></tr>
</table>
</form>

</body>
</html>
<?php
}
?>
