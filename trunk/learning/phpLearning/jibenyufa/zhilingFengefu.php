<?php
    echo '此句后有分号<br/>';
?>
<?php echo '此句后无分号<br/>'?>
<!--
     同 C 或 Perl 一样，PHP 需要在每个语句后用分号结束指令。一段 PHP 代码中的结束标记隐含表示了一个分号；在一个 PHP 代码段中的最后一行可以不用分号结束。如果后面还有新行，则代码段的结束标记包含了行结束。
<?php
    echo "This is a test";
?>
<?php echo "This is a test" ?>
    注: 文件末尾的 PHP 代码段结束标记可以不要，有些情况下当使用输出缓冲和 include() 或者 require() 时省略掉会更好些。
-->