<h2>1.return()</h2>
<?php
    function salestax($price, $tax=0.575){
        $total = $price + ($price * $tax);
        //return $total;
        return $price + ($price * $tax);
    }

    $price = 6.50;
    $total = salestax($price);
    echo "Total cost is $total"."<br/>";
?>

<h2>2.返回多个值</h2>
<?php
    $colors = array(
        "red",
        "yellow",
        "green",
    );
    list($red,$yellow,$green) = $colors;
    echo $red." ".$yellow." ".$green."<br/>";


    function retrieve_user_profile(){
        $user[] = "Crackpot";
        $user[] = "gaofeitop@gmail.com";
        $user[] = "Chinese";
        return $user;
    }
    list($name,$email,$language) = retrieve_user_profile();
    echo "Name : $name <br/> Email : $email <br/> Preferred language : $language"."<br/>";
?>
