<?php
    $ms_office = array(
        'wd'=>'word',
        'ec'=>'excel',
        'ol'=>'outlook',
        'ac'=>'access',
        'vs'=>'visio'
    );

    echo '<pre>';
    print_r(array_chunk($ms_office,2));
    print_r(array_chunk($ms_office,2,TRUE));
?>
