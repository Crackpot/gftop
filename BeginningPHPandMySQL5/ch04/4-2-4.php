<?php
    function salestax($price,$tax=""){
        $total = $price + ($price * $tax);
        echo "Total cost is ".$total."<br/>";
    }
    salestax (42.00);
?>
<?php
    function calculate($price,$price2="",$price3=""){
        echo "Total cost is ".($price + $price2 + $price3);
    }
    calculate(10,"",3);
?>
