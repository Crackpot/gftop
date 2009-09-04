<title>字符串插入</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<h3>字符串插入</h3>
<h5>3.9.1 双引号</h5>
<?php
    $sport = "boxing";
    echo "Jason's favorite sport is $sport"."<br/>";
?>
<?php
    $output = "This is one line.\nAnd this is another line."."<br/>";
    echo $output;
?>
<h5>3.9.2 单引号</h5>
<?php
    echo 'This is another string.\\';
?>
<h5>3.9.3 Heredoc</h5>
<p>
    &nbsp;&nbsp;&nbsp;&nbsp;
    Heredoc语法为输出大量文本提供了一种便利的方式。它不是使用双引号或者单引号来界定字符串，而是采用了两个相同的标识符。
</p>
<?php
    $website = "http://www.romatemini.it";
    echo <<<EXCERPT
    <p>Rome's central train station, known as <a href = "$website">Roma Termini</a>,
    was built in 1867.Because it had fallen into severe disrepair in the late 20th
    century, the government knew that considerable resources were required to
    rehabilitate the station prior to the 50-year <i>Giubileo</i>.</p>
EXCERPT;
?>
