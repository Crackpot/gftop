<!--
    高级分离术
    当 PHP 碰到结束标记 ?>  时，就简单地将其后的内容原样输出直到碰到下一个开始标记为止。当然，上面的例子很做作，但是对输出大块的文本而言，脱离 PHP 解析模式通常比将所有内容用 echo()  或者 print() 输出更有效率。
    可以在 PHP 中使用四对不同的开始和结束标记。其中两种，<?php ?> 和 <script language="php"> </script> 总是可用的。另两种是短标记和 ASP 风格标记，可以在 php.ini 配置文件中打开或关闭。尽管有些人觉得短标记和 ASP 风格标记很方便，但移植性较差，通常不推荐。 
-->
<?php
    $a=1;
    if ($a){
        ?>
        <strong>a的值为1。</strong><br/>
        <?php
    }
    else{
        ?>
        <strong>a的值不为1。</strong><br/>
        <?php
    }
?>
<script language="php">
    $a=1;
    if ($a){
</script>
    <strong>a的值为1。</strong><br/>
<script language="php">
    }
    else{
</script>
    <strong>a的值不为1。</strong><br/>
<script language="php">
    }
</script>