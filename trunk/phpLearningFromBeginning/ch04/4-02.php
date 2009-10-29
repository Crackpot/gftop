<?php
    $ms_office = array(
        'word',
        'excel',
        'outlook',
        'access',
    );

    for($i = 0; $i < 4; $i ++)
    {
        echo "数组第 ".($i + 1)." 个元素是：";
        echo $ms_office[$i]."<br/>";
        echo "<br/>";
    }
?>
