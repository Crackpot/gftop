<?php
    define(PI,3.14);

    for($r = 3; $r<=8; $r++)
    {
        $s = get_circle_area($r);
        echo "r=$r, area=$s"."<br/>";
        echo "<br/>";
    }

    function get_circle_area($radius)
    {
        $area = PI * $radius * $radius;
        return $area;
    }
?>
