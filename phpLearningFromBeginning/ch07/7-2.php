<?php
echo "ʱ���".mktime(0,0,0,12,31,2007)."��Ӧ�������ǣ�";
echo "<br/>";

echo date("M-d-Y", mktime(0,0,0,12,31,2007));
echo "<hr>";
echo "<br/>";

$day = 1;
echo "ʱ���".mktime(0,0,0,7,$day+38,2008)."��Ӧ�������ǣ�<br/>";
echo date("Y-m-d", mktime(0,0,0,7,$day+38,2008));
echo "<hr>";
?>