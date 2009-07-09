<?php
$user_name = $_POST['user_name'];
$gender = $_POST['gender'];
$hobby = $_POST['hobby'][0]."、".$_POST['hobby'][1]."、 ".$_POST['hobby'][2]."、 ".$_POST['hobby'][3];
$prof = $_POST['occup'];

//当用户名为空，即没有输入用户名时，则输出一个提示信息，并中断程序的执行
if($user_name == "")
{
	echo "请返回输入用户名！";
	exit;    //exit语句将使程序立即中断，不再向下执行。
}

if($gender == "")
{
	echo "请返回选择性别！";
	exit;
}

if($hobby == "")
{
	echo "请返回选择兴趣与爱好！";
	exit;
}

echo "用户名：".$user_name."<br/>";
echo "性别：".$gender."<br/>";
echo "爱好：".$hobby."<br/>";
echo "职业：".$prof."<br/>";
?>