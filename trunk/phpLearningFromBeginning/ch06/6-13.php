<?php
$last_access = fileatime("data.txt");
echo "�ļ����ķ���ʱ���ǣ�";
echo date("l F d, Y", $last_access);
echo "<br>";
echo "<br>";

$last_modify = filemtime("data.txt");
echo "�ļ������޸�ʱ�䣺";
echo date("l F d, Y", $last_modify);
echo "<br>";
echo "<br>";

$last_modify_inode = filectime("data.txt");
echo "�ļ����ĸı�ʱ�䣺";
echo date("l F d, Y", $last_modify_inode);
echo "<br>";
echo "<br>";
?>