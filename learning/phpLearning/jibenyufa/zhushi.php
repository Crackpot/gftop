<p> PHP 支持 C，C++ 和 Unix Shell 风格（Perl 风格）的注释。 </p>
<?php
     echo "This is a test<br/>"; // This is a one-line c++ style comment
    /* This is a multi line comment
       yet another line of comment */
    echo "This is yet another test<br/>";
    echo "One Final Test<br/>"; # This is shell-style style comment
?>
<p>单行注释仅仅注释到行末或者当前的 PHP 代码块，视乎哪个首先出现。这意味着在 // ?> 之后的 HTML 代码将被显示出来：?>  跳出了 PHP 模式并返回了 HTML 模式，//  并不能影响到这一点。如果启用了 asp_tags 配置选项，其行为和 // %> 相同。不过，</script>  标记在单行注释中不会跳出 PHP 模式。</p>
