<h3>表达式</h3>

<h5>先来几个例子</h5>
<?php
   $a = 5; 
   echo "a = $a"."，其类型为：".gettype($a)."<br/>";
   $a = "5"; 
   echo "a = $a"."，其类型为：".gettype($a)."<br/>";
   echo "some_int = $some_int"."，其类型为：".gettype($some_int)."<br/>";
   $sum = 50 + $some_int;
   echo "sum = $sum"."，其类型为：".gettype($sum)."<br/>";
   $wine ="Zinfandel";
   echo "wine = $wine"."，其类型为：".gettype($wine)."<br/>";
   echo "inventory = $inventory"."，其类型为：".gettype($inventory)."<br/>";
   $inventory++;
   echo "inventory = $inventory"."，其类型为：".gettype($inventory)."<br/>";
?>

<h5>3.8.1 操作数</h5>
<?php
   $a++;
   echo "a = $a"."，其类型为：".gettype($a)."<br/>";
   $sum = $val1 + $val2;
   echo "val1 = $val1"."，其类型为：".gettype($val1)."<br/>";
   echo "val2 = $val2"."，其类型为：".gettype($val2)."<br/>";
   echo "\$sum = \$val1 + \$val2 =".($val1 + $val2)."，其类型为：".gettype($a)."<br/>";
?>

<h5>3.8.2 操作符</h5>
<?php
   echo "1、操作符优先级"."<br/>";
   $cost = 0.3;
   echo "\$cost = $cost"."<br/>";
   $totalcost = $cost + $cost * 0.96;
   echo "\$totalcost = \$cost + \$cost * 0.96 = $totalcost"."<br/>";
   echo "上式相当于：<br/>\$totalcost = \$cost + (\$cost * 0.96) = $totalcost"."<br/>";


   echo "<br/>";
   echo "2、操作符结合性"."<br/>";
   $value = 3 * 4 * 5 * 6 * 7;
   echo "\$value = 3 * 4 * 5 * 6 * 7 = $value"."<br/>";
   echo "上式相当于：<br/>\$value = ((((3 * 4) * 5) * 6) * 7) = $value"."<br/>";


   echo "<br/>";
   echo "3、算术操作符"."<br/>";
   $a = 537;
   $b = 124;
   echo "\$a = $a"."<br/>";
   echo "\$b = $b"."<br/>";
   echo "加： \$a + \$b =".($a + $b)."<br/>";
   echo "减： \$a - \$b =".($a - $b)."<br/>";
   echo "乘： \$a * \$b =".($a * $b)."<br/>";
   echo "除： \$a / \$b =".($a / $b)."<br/>";
   echo "模： \$a % \$b =".($a % $b)."<br/>";

   echo "<br/>";
   echo "4、赋值操作符"."<br/>";
   $a = 604;
   echo "\$a = $a"."<br/>";
   echo "\$a += 3 ==> \$a = ".($a + 3)."<br/>";
   echo "\$a -= 3 ==> \$a = ".($a - 3)."<br/>";
   echo "\$a *= 3 ==> \$a = ".($a * 3)."<br/>";
   echo "\$a /= 3 ==> \$a = ".($a / 3)."<br/>";
   echo "\$a %= 3 ==> \$a = ".($a % 3)."<br/>";

   echo "<br/>";
   echo "5、字符串操作符"."<br/>";
   $a = "abc"."def";
   echo "拼接： \$a = \"abc\".\"def = $a"."<br/>";
   $a .= "ghijkl";
   echo "拼接赋值： \$a .= \"ghijkl\" = $a"."<br/>";

   echo "<br/>";
   echo "6、自增和自减操作符"."<br/>";
   $a = 3;
   echo "\$a = $a"."<br/>";
   echo "\$++a = ".++$a." 先增加后使用 <br/>";
   echo "\$a++ = ".$a++." 先使用后增加 <br/>";
   echo "\$a = $a"."<br/>";
   echo "\$--a = ".--$a." 先减小后使用 <br/>";
   echo "\$a-- = ".$a--." 先使用后减小 <br/>";
   echo "\$a = $a"."<br/>";

   echo "<br/>";
   echo "7、逻辑操作符"."<br/>";
   $a = 1;
   $b = 0;
   echo "\$a = $a"."<br/>";
   echo "\$b = $b"."<br/>";
   echo "\$a && \$b = ".($a && $b)."<br/>";
   echo "\$a and \$b = ".($a and $b)."<br/>";
   echo "\$a || \$b = ".($a || $b)."<br/>";
   echo "\$a or \$b = ".($a or $b)."<br/>";
   echo "!\$a = ".!$a."<br/>";
   echo "!\$b = ".!$b."<br/>";
   echo "\$a xor \$b = ".($a xor $b)."<br/>";
   file_exists("hello.html") or print "File hello.html does not exists<br/>";

   echo "<br/>";
   echo "8、相等操作符"."<br/>";
   $a = "hello";
   $b = "hello";
   echo "\$a = $a"."<br/>";
   echo "\$b = $b"."<br/>";
   echo "\$a == \$b = ".($a == $b)."<br/>";
   echo "\$a != \$b = ".($a != $b)."<br/>";
   echo "\$a === \$b = ".($a === $b)."<br/>";

   echo "<br/>";
   echo "9、比较操作符"."<br/>";
   $a = 1;
   $b = 0;
   echo "\$a = $a"."<br/>";
   echo "\$b = $b"."<br/>";
   echo "\$a < \$b = ".($a < $b)."<br/>";
   echo "\$a <= \$b = ".($a <= $b)."<br/>";
   echo "\$a > \$b = ".($a > $b)."<br/>";
   echo "\$a >= \$b = ".($a >= $b)."<br/>";
   $c = ($a == 12)? "\$a是12" : "\$a不是12";
   echo "\$c = (\$a == 12)? \"\$a是12\" : \"\$a不是12\"<br/>";
   echo "\$c = $c"."<br/>";

   echo "<br/>";
   echo "10、位操作符"."<br/>";
   $a = 16;
   $b = 5;
   echo "\$a = $a"."<br/>";
   echo "\$b = $b"."<br/>";
   echo "与运算： \$a & \$b =".($a & $b)."<br/>";
   echo "或运算： \$a | \$b =".($a | $b)."<br/>";
   echo "异或运算： \$a ^ \$b =".($a ^ $b)."<br/>";
   echo "非运算： ~\$a =".(~ $a)."<br/>";
   echo "非运算： ~\$b =".(~ $b)."<br/>";
   echo "左移运算：<br/>";
   echo "\$a << 2 ==> \$a =".($a << 2)."<br/>";
   echo "\$a << 3 ==> \$a =".($a << 3)."<br/>";
   echo "\$a << 4 ==> \$a =".($a << 4)."<br/>";
   echo "右移运算：<br/>";
   echo "\$a >> 2 ==> \$a =".($a >> 2)."<br/>";
   echo "\$a >> 3 ==> \$a =".($a >> 3)."<br/>";
   echo "\$a >> 4 ==> \$a =".($a >> 4)."<br/>";
   echo ""."<br/>";
?>
