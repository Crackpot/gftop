<?php
    $arr1 = array('Earth','Venus');
    #Earth下标为0，Venus下标为1
    $arr2 = array(4=>'Mars',5=>'Jupiter',6=>'Saturn');

    $planet = array_merge($arr1,$arr2);
    echo '<pre>';
    print_r($planet);
?>
