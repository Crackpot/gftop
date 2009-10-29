<?php
    $cellphone_brand = array(
        'nokia',
        'moto',
        'lenovo',
        'tcl'
    );

    echo '原数组：'."<br/>";
    echo '<pre>';
    print_r($cellphone_brand);
    echo '</pre>';

    shuffle($cellphone_brand);
    echo '<br/>';

    echo '元素被重新排序后：';
    echo '<br/>';
    echo '<br/>';

    foreach ($cellphone_brand as $cpb){
        echo $cpb.'  ';
    }
?>
