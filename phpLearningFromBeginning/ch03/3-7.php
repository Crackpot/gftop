<?php
//���ļ������������ĸ�Ŀ¼��uploadĿ¼�£�upload���ȵý�����
$upload_path = $_SERVER['DOCUMENT_ROOT']."/upload/";
$dest_file = $upload_path.basename($_FILES['myfile']['name']);

if(move_uploaded_file($_FILES['myfile']['tmp_name'],$dest_file))
{
	echo "�ļ����ϴ�����������Ŀ¼��uploadĿ¼��";
}
else
{
	echo "�ļ��ϴ�ʱ������һ������".$_FILES['myfile']['error'];	
}
?>