<?php
echo mt_rand();
echo "<br/>";
echo mt_rand(100,999);
echo "<hr/>";

echo "以下通过循环生成1-100之间的多个随机数<br/>";
for($i = 0; $i < 10; ++$i)
{
    $number = (mt_rand()%100)+1;
    echo "$number<br/>";
}
?>
