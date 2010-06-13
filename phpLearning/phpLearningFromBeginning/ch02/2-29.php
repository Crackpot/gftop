<?php
    define(PI,3.14);

    for($r = 1; $r <= 10; $r ++)
    {
        $area = PI * $r * $r;
        if($area > 150)
            break;

        echo "r = $r , area = $area"."<br/>";
        echo "<br/>";
    }
?>
