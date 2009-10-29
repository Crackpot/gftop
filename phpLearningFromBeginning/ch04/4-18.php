<?php
    echo '<pre>';

    echo "range 将范围内的元素归为数组元素"."<br/>";
    echo '<br/>';

    $arr1 = range(5,10);
    print_r($arr1);

    $arr2 = range('a','f');
    print_r($arr2);

    $arr3 = range(2,10,2);
    print_r($arr3);
    echo '</pre>';
?>
