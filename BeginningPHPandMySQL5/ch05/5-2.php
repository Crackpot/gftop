<h1>输出数组</h1>
<?php
    $states = array(
        "Ohio" => "Columbus",
        "Iowa" => "Des Moines",
        "Arizona" => "Phoenix",
    ); 

    echo "数组states为："."<br/>";
    print_r($states);
    echo "<pre>";
    print_r($states);
    echo "</pre>";

    $statesCaptitals = print_r($states,TRUE);
    echo $statesCaptitals."<br/>";
    $statesCaptitals = print_r($states,FALSE);
    echo $statesCaptitals."<br/>";
?>
