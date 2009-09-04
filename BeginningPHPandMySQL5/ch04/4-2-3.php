<?php
    function salestax($price, $tax = 0.575){
        $total = $price + ($price * $tax);
        echo "Total cost is ".$total."<br/>";
    }
?>
<?php
    $price = 15.47;
    salestax($price);
?>
