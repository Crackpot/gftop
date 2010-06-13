<?php
$user_name = $_POST['user_name'];    //通过$_POST全局变量，获取表单元素传入的数据，并赋给变量
$gender = $_POST['gender'];
$hobby = $_POST['hobby'][0]."、".$_POST['hobby'][1]."、 ".$_POST['hobby'][2]."、 ".$_POST['hobby'][3];
$prof = $_POST['occup'];

echo "用户名：".$user_name;
echo "<br/>";
echo "<br/>";

echo "性别：".$gender;
echo "<br/>";
echo "<br/>";

echo "爱好：".$hobby;
echo "<br/>";
echo "<br/>";

echo "职业：".$prof;
?>
