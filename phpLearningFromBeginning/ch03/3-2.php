<?php
$user_name = $_POST['user_name'];    //ͨ��$_POSTȫ�ֱ�������ȡ��Ԫ�ش�������ݣ�����������
$gender = $_POST['gender'];
$hobby = $_POST['hobby'][0]."��".$_POST['hobby'][1]."�� ".$_POST['hobby'][2]."�� ".$_POST['hobby'][3];
$prof = $_POST['occup'];

echo "�û�����".$user_name;
echo "<br/>";
echo "<br/>";

echo "�Ա�".$gender;
echo "<br/>";
echo "<br/>";

echo "���ã�".$hobby;
echo "<br/>";
echo "<br/>";

echo "ְҵ��".$prof;
?>