1.  <?php echo 'if you want to serve XHTML or XML documents, do like this'; ?><br/>

2.  <script language="php">
        echo 'some editors (like FrontPage) don\'t
              like processing instructions';
    </script><br/>

3.  <? echo 'this is the simplest, an SGML processing instruction'; ?>
    <?= expression ?> This is a shortcut for "<? echo expression ?>"<br/>

4.  <% echo 'You may optionally use ASP-style tags'; %>
    <%= $variable; # This is a shortcut for "<% echo . . ." %><br/>
     此例中的 1 和 2 总是可用的，其中 1 是最常用，并建议使用的。

短标记（此例 3）仅在通过 php.ini 配置文件中的指令 short_open_tag 打开后才可用，或者在 PHP 编译时加入了 --enable-short-tags 选项。

    注: 如果用 PHP 3 还可以通过 short_tags() 函数激活使用短标记。此方法只适用于 PHP 3！ 

ASP 风格标记（此例 4）仅在通过 php.ini 配置文件中的指令 asp_tags 打开后才可用。

    注: 对 ASP 风格标记的支持是 3.0.4 版添加的。 

    注: 在以下情况应避免使用短标记：开发需要发行的程序或者库，或者在用户不能控制的服务器上开发。因为目标服务器可能不支持短标记。为了代码的移植及发行，确保不要使用短标记。 