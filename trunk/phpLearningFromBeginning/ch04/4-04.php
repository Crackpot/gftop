<?php
    $ms_office = array(
        'wd'=>'word',
        'ec'=>'excel',
        'ol'=>'outlook',
        'ac'=>'access',
    );

    foreach($ms_office as $key=>$value){
        echo $key.": ".$value;
        echo "<br/>";
        echo "<br/>";
    }
?>
