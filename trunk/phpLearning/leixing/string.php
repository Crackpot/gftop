<p>
    <h3>字符串</h3>

string 是一系列字符。在 PHP 中，字符和字节一样，也就是说，一共有 256 种不同字符的可能性。这也暗示 PHP 对 Unicode 没有本地支持。请参阅函数 utf8_encode() 和 utf8_decode() 以了解有关 Unicode 支持。<br/>

    注: 一个字符串变得非常巨大也没有问题，PHP 没有给字符串的大小强加实现范围，所以完全没有理由担心长字符串。 <br/>

<br/><strong>语法</strong><br/>

字符串可以用三种字面上的方法定义。<br/>

    *      单引号<br/>
    *      双引号<br/>
    *      定界符<br/>

<br/><strong>单引号</strong><br/>

指定一个简单字符串的最简单的方法是用单引号（字符 '）括起来。<br/>

要表示一个单引号，需要用反斜线（\）转义，和很多其它语言一样。如果在单引号之前或字符串结尾需要出现一个反斜线，需要用两个反斜线表示。注意如果试图转义任何其它字符，反斜线本身也会被显示出来！所以通常不需要转义反斜线本身。<br/>    

    注: 和其他两种语法不同，单引号字符串中出现的变量和转义序列不会被变量的值替代。 <br/>
</p>
<?php
    echo 'this is a simple string<br/>';

    echo 'You can also have embedded newlines in
    strings this way as it is
    okay to do<br/>';

    // Outputs: Arnold once said: "I'll be back"
    echo 'Arnold once said: "I\'ll be back"<br/>';

    // Outputs: You deleted C:\*.*?
    echo 'You deleted C:\\*.*?<br/>';

    // Outputs: You deleted C:\*.*?
    echo 'You deleted C:\*.*?<br/>';

    // Outputs: This will not expand: \n a newline
    echo 'This will not expand: \n a newline<br/>';

    // Outputs: Variables do not $expand $either
    echo 'Variables do not $expand $either<br/>';
?>
<p>
    <br/><strong>双引号</strong><br/>
    如果用双引号（"）括起字符串，PHP 懂得更多特殊字符的转义序列：<br/>

    <br/><strong>转义字符</strong><br/>
    <table border="1">
        <tr align="center" bgcolor="green">
            <td>序列</td>
            <td>含义</td>
        </tr>
        <tr>
            <td>\n</td>
            <td>换行（LF 或 ASCII 字符 0x0A（10））</td>
        </tr>
        <tr>
            <td>\r</td>
            <td>回车（CR 或 ASCII 字符 0x0D（13））</td>
        </tr>
        <tr>
            <td>\t</td>
            <td>水平制表符（HT 或 ASCII 字符 0x09（9）</td>
        </tr>
        <tr>
            <td>\\</td>
            <td>反斜线</td>
        </tr>
        <tr>
            <td>\$</td>
            <td>美元符号</td>
        </tr>
        <tr>
            <td>\"</td>
            <td>双引号</td>
        </tr>
        <tr>
            <td>\[0-7]{1,3}</td>
            <td>此正则表达式序列匹配一个用八进制符号表示的字符</td>
        </tr>
        <tr>
            <td>\x[0-9A-Fa-f]{1,2}</td>
            <td>此正则表达式序列匹配一个用十六进制符号表示的字符</td>
        </tr>
    </table>
    <br/>
此外，如果试图转义任何其它字符，反斜线本身也会被显示出来！<br/>

双引号字符串最重要的一点是其中的变量名会被变量值替代。细节参见字符串解析。 <br/>
<br/><strong>定界符</strong><br/>

另一种给字符串定界的方法使用定界符语法（“<<<”）。应该在 <<< 之后提供一个标识符，然后是字符串，然后是同样的标识符结束字符串。<br/>

结束标识符必须从行的第一列开始。同样，标识符也必须遵循 PHP 中其它任何标签的命名规则：只能包含字母数字下划线，而且必须以下划线或非数字字符开始。<br/>

警告<br/>

很重要的一点必须指出，结束标识符所在的行不能包含任何其它字符，可能除了一个分号（;）之外。这尤其意味着该标识符不能被缩进，而且在分号之前和之后都不能有任何空格或制表符。同样重要的是要意识到在结束标识符之前的第一个字符必须是你的操作系统中定义的换行符。例如在 Macintosh 系统中是 \r。<br/>

如果破坏了这条规则使得结束标识符不“干净”，则它不会被视为结束标识符，PHP 将继续寻找下去。如果在这种情况下找不到合适的结束标识符，将会导致一个在脚本最后一行出现的语法错误。<br/>

不能用定界符语法初始化类成员。用其它字符串语法替代。<br/>
</p>
<?php
    $str = <<<EOD
Example of string
spanning multiple lines
using heredoc syntax.<br/>
EOD;
    echo $str;
    /* More complex example, with variables. */
    class foo{
        var $foo;
        var $bar;
        function foo(){
            $this->foo='Foo';
            $this->bar=array('Bar1','Bar2','Bar3');
        }
    }
    $foo=new foo();
    $name="Crackpot";
    echo <<<EOT
My name is "$name".
I am printing some $foo->foo.
Now, I am printing some {$foo->bar[1]}.
This should print a capital 'A': \x41
EOT;
?>
<p>
    <h3>变量解析</h3>

当用双引号或者定界符指定字符串时，其中的变量会被解析。<br/>

有两种语法，一种简单的和一种复杂的。简单语法最通用和方便，它提供了解析变量，数组值，或者对象属性的方法。<br/>

复杂语法是 PHP 4 引进的，可以用花括号括起一个表达式。<br/>
<br/><strong>简单语法</strong><br/>


如果遇到美元符号（$），解析器会尽可能多地取得后面的字符以组成一个合法的变量名。如果想明示指定名字的结束，用花括号把变量名括起来。<br/> 
</p>
<?php
    $beer = 'Heineken';
    echo "$beer's taste is great<br/>"; // works, "'" is an invalid character for varnames
    echo "He drank some $beers<br/>";   // won't work, 's' is a valid character for varnames
    echo "He drank some ${beer}s<br/>"; // works
    echo "He drank some {$beer}s<br/>"; // works
?>
<p >同样也可以解析数组索引或者对象属性。对于数组索引，右方括号（]）标志着索引的结束。对象属性则和简单变量适用同样的规则，尽管对于对象属性没有像变量那样的小技巧。
</p>
<?php
    // These examples are specific to using arrays inside of strings.
    // When outside of a string, always quote your array string keys
    // and do not use {braces} when outside of strings either.

    // Let's show all errors
    error_reporting(E_ALL);
    $fruits = array(
        'strawberry' => 'red',
        'banana' => 'yellow',
        '香蕉'=>'黄色的',
        );
    // Works but note that this works differently outside string-quotes
    echo "A banana is $fruits[banana].<br/>";
    echo "香蕉是$fruits[香蕉]。<br/>";
    //Works
    echo "A banana is {$fruits[banana]}.<br/>";
    echo "香蕉是$fruits[香蕉]。<br/>";
    // Works but PHP looks for a constant named banana first as described below.
echo "A banana is {$fruits[banana]}.";

    // Won't work, use braces.  This results in a parse error.
    //echo "A banana is $fruits['banana'].";加了引号

    // Works
    echo "A banana is " . $fruits['banana'] . ".";

    // Works
    echo "This square is $square->width meters broad.";
    // Won't work. For a solution, see the complex syntax.
    echo "This square is $square->width00 centimeters broad.";
?>
<p >
    对于任何更复杂的情况，应该使用复杂语法。<br/>
    <br/><strong>复杂（花括号）语法</strong><br/>

不是因为语法复杂而称其为复杂，而是因为用此方法可以包含复杂的表达式。<br/>

事实上，用此语法可以在字符串中包含任何在名字空间的值。仅仅用和在字符串之外同样的方法写一个表达式，然后用 { 和 } 把它包含进来。因为不能转义“{”，此语法仅在 $ 紧跟在 { 后面时被识别（用“{\$”或者“\{$”来得到一个字面上的“{$”）。用一些例子可以更清晰： <br/>
</p>
<?php
    // Let's show all errors
    error_reporting(E_ALL);
    $great = 'fantastic';
    echo "This is $great!<br/>";
    echo "This is {$great}!<br/>";
    echo "This is ${great}!<br/>";
    echo "This square is {$square->width}00 centimeters broad.";
?>