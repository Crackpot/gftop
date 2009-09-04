<?php
    echo "\$Spaghetti = $Spaghetti"."<br/>";
    $recipe = "Spaghetti";
    echo "\$recipe = $recipe"."<br/>";
    $$recipe = "& meatballs";
    echo "\$\$recipe = ".$$recipe."<br/>";
    echo "\$\$recipe = ".${$recipe}."<br/>";
    echo "\$Spaghetti = $Spaghetti"."<br/>";
?>
