<?php
    $count = 1;
    for($a = 100; $a <= 200; $a ++)
    {
        if($a % 2 == 0)
            continue;
        echo $a."\t";
        #echo $a."<br/>";
        if ($count % 10 == 0){
            #一行10个数
            echo "<br/>";
        }
        $count ++;
    }
?>
