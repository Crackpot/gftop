<?php
    echo "对于这段代码，可以传递以下URL：http://www.example.com/index.php?trigger=retrieveUser&rowid=5"."<br/>";
    if($trigger == "retrieveUser"){
        retrieveUser($rowid);
    }
    elseif($trigger == "retrieveNews"){
        retrieveNews($rowid);
    }
    elseif($trigger == "retrieveWeather"){
        retrieveWeather($rowid);
    }
?>
<?php
    echo "简化";
    $trigger($rowid);
?>
