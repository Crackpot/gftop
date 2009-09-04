<?php
    function salestax($price,$tax){
        $total = $price + ($price * $tax);
        echo "Total cost: $total";
    }
?>
<?php
    $pricetag = 15.00;
    $salestax = .75;
    salestax($pricetag,$salestax);
?>
