<?php
$fp = fopen($_SERVER['DOCUMENT_ROOT']."/../data/lock_test.txt",'w');

flock($fp,LOCK_EX);    //д����������˵���ļ�lock_test.txt
fwrite($fp,"Write Some Words....");
flock($fp,LOCK_UN);    //�ͷŶ��ļ�lock_test.txt������

fclose($fp);
?>