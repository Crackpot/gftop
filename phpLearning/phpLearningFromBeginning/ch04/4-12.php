<?php
    $planet = array(
        'Earth',
        'Venus',
        'Mars',
        'Jupiter',
        'Saturn'
    );

    echo "<pre>";
    print_r($planet);
    echo "<br/>";
    echo "</pre>";

    rsort($planet);

    foreach($planet as $key => $value)
    {
        echo 'planet['.$key.']='.$value."<br/>";
        echo '<br/>';
    }
?>
