<?php
$user_name = $_POST['user_name'];
$gender = $_POST['gender'];
$hobby = $_POST['hobby'][0]."��".$_POST['hobby'][1]."�� ".$_POST['hobby'][2]."�� ".$_POST['hobby'][3];
$prof = $_POST['occup'];

//���û���Ϊ�գ���û�������û���ʱ�������һ����ʾ��Ϣ�����жϳ����ִ��
if($user_name == "")
{
	echo "�뷵�������û�����";
	exit;    //exit��佫ʹ���������жϣ���������ִ�С�
}

if($gender == "")
{
	echo "�뷵��ѡ���Ա�";
	exit;
}

if($hobby == "")
{
	echo "�뷵��ѡ����Ȥ�밮�ã�";
	exit;
}

echo "�û�����".$user_name."<br/>";
echo "�Ա�".$gender."<br/>";
echo "���ã�".$hobby."<br/>";
echo "ְҵ��".$prof."<br/>";
?>