<?php
    $planet = array(
        'Earth',
        'Venus',
        'Mars',
        'Jupiter',
        'Saturn',
    );

    echo "<pre>";
    print_r($planet);
    echo "<br/>";
    echo "</pre>";

    sort($planet);//将数组中的各个元素按照首字母的顺序排序

    foreach($planet as $key => $value)
    {
        echo 'planet['.$key.']='.$value."<br/>";
        echo '<br/>';
    }
?>
