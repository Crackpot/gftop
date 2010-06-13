<?php
$num = 123;
$long = 753159852;
$float = 0.45;
$str = "banana";

printf("%%d = %d<br/>",$num);
printf("%%b = %b<br/>",$num);
printf("%%e = %e<br/>",$long);
printf("%%f = %f<br/>",$num);
printf("%%f = %01.2f<br/>",$num);
printf("%%f = %03.5f<br/>",$float);
printf("%%f = %08.4f<br/>",$float);

echo "<br/>";

printf("[%s]<br/>",$str);
printf("[%8s]<br/>",$str);
printf("[%-8s]<br/>",$str);
printf("[%08s]<br/>",$str);
printf("[%'$8s]<br/>",$str);
?>