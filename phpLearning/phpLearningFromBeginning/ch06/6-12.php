<?php
$fp = fopen($_SERVER['DOCUMENT_ROOT']."/../data/lock_test.txt",'w');

flock($fp,LOCK_EX);    //写锁定，独享说定文件lock_test.txt
fwrite($fp,"Write Some Words....");
flock($fp,LOCK_UN);    //释放对文件lock_test.txt的锁定

fclose($fp);
?>
