<?php
echo mt_rand();
echo "<br/>";
echo mt_rand(100,999);
echo "<hr/>";

echo "����ͨ��ѭ������1-100֮��Ķ�������<br/>";
for($i = 0; $i < 10; ++$i)
{
    $number = (mt_rand()%100)+1;
    echo "$number<br/>";
}
?>