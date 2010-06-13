<?php
    $ms_office = array(
        'word',
        'excel',
        'outlook',
        'access',
    );

    $count = 0;
    foreach($ms_office as $software){
        echo "数组中第".$count."个元素为：".$software."<br/>";
        echo "<br/>";
        $count ++;
    }
?>
