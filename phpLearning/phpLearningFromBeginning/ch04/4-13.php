<?php
    $planet1 = array(
        'Earth',
        'Venus',
        'Mars',
        'Jupiter',
        'Saturn'
    );

    $planet2 = array(
        'X'=>'Earth',
        'Y'=>'Venus',
        'Z'=>'Mars',
        'A'=>'Jupiter',
        'B'=>'Saturn'
    );

    echo "原始数组为："."<br/>";
    echo "\$planet1 ==> ";
    print_r($planet1);
    echo "<br/>";
    echo "\$planet2 ==> ";
    print_r($planet2);
    echo "<br/>";

    asort($planet1);
    ksort($planet2);

    echo "<br/>";
    echo '使用函数asort对数组元素排序：(首字母顺序排序)';
    echo '<br/>';

    foreach($planet1 as $key => $value)
    {
        echo 'planet1['.$key.']='.$value;
        echo '<br/>';
        echo '<br/>';
    }

    echo '<br/>';  
    echo '使用函数ksort对数组元素排序：(关联顺序排序)';
    echo '<br/>';

    foreach($planet2 as $key => $value)
    {
        echo 'planet2['.$key.']='.$value;
        echo '<br/>';
        echo '<br/>';
    }
?>
