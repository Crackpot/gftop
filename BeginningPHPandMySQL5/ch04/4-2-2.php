<?php
    $cost = 20.00;
    $tax = 0.05;

    echo "调用函数calculate_cost前:"."<br/>";
    echo "Tax is : ".($tax*100)."% <br/>";
    echo "Cost is : ".$cost."<br/>";

    function calculate_cost(&$cost, $tax){
        // Modify the $cost variable
        $cost = $cost + ($cost * $tax);
        // Perform some random change to the $tax variable.
        $tax += 4;
    }
    calculate_cost($cost,$tax);

    echo "<br/>";
    echo "调用函数calculate_cost后:"."<br/>";
    echo "Tax is : ".($tax*100)."% <br/>";
    echo "Cost is : ".$cost."<br/>";
?>
