<?php
$a = 100;

echo "����ǰ������\$a�������ǣ�".gettype($a);
echo "<br/>";
echo "<br/>";

settype($a,"string");
echo "���ú󣬱���\$a�������ǣ�".gettype($a);
?>