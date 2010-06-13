<?php
    $planet = array(
        'Earth',
        'Venus',
        'Mars',
        'Jupiter',
        'Saturn',
    );

    echo "<pre>";
    print_r($planet);//打印整个数组
    echo '<br/>';
    echo '</pre>';

    $pos = current($planet);  //此时$pos=Earth，为数组的0元素
    echo 'pos1='.$pos."<br/>";
    echo '<br/>';

    $pos = next($planet);     //此时$pos=Venus，后移一个下标
    echo 'pos2='.$pos."<br/>";
    echo '<br/>';

    $pos = current($planet);  //此时$pos=Venus
    echo 'pos3='.$pos."<br/>";
    echo '<br/>';

    $pos = prev($planet);     //此时$pos=Earth
    echo 'pos4='.$pos."<br/>";
    echo '<br/>';

    $pos = end($planet);      //此时$pos=Saturn
    echo 'pos5='.$pos."<br/>";
    echo '<br/>';

    $pos = current($planet);  //此时$pos=Saturn
    echo 'pos6='.$pos."<br/>";
?>
