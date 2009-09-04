<h2>1.计算总价</h2>
<?php
    function salestax($price,$tax){
        function convert_pound($dollars,$convertion=1.6){
            return $dollars * $convertion;
        }
        $total = $price + ($price * $tax);
        echo "Total cost in dollars : $total . Cost in British pounds : ".convert_pound($total)."<br/>";
    }
    salestax(15.00,.075);
    echo convert_pound(15);
?>

<h2>2.乘法表</h2>
<?php
    echo "<table>"; 
    for($i = 1; $i <= 9; $i ++){
        echo "<tr>";
        for($j = 1; $j <= $i; $j ++){
            echo "<td bgcolor='green'>&nbsp;".$i." * ".$j." = ".($i*$j)."&nbsp;</td>";
        }
        echo "</tr>";
    }
    echo "</table>";
?>
