<?php
    $ms_office = array(
        'word',
        'excel',
        'outlook',
        'access',
    );

    echo "<pre>";
    print_r($ms_office);

    echo "<br/>";
    $item_num = count($ms_office);
    echo '数组$ms_office的元素个数为：'.$item_num;
?>
