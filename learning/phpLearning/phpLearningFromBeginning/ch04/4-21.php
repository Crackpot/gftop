<?php
    $olympic = array(
        'Barcelona'=>1992,
        'AtLanTa'=>1996,
        'sydney'=>2000,
        'AthEns'=>2004,
        'BEIJING'=>2008
    );

    echo '原数组：';
    echo '<pre>';
    print_r($olympic);
    echo '</pre>';

    $nol = array_change_key_case($olympic, CASE_UPPER);
    echo '<br/>';

    echo '调用array_change_key_case()之后：';
    echo '<pre>';
    print_r($nol);
?>
