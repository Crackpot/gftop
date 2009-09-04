<h1>循环语句</h1>

<h2>1.while</h2>
<?php
    $count = 1;
    echo "while语句中千万不要忘记写变量变化语句"."<br/>";
    while ($count < 5){
        echo "$count squared = ".pow($count,2)."<br/>";
        $count ++;
    }
?>
<p/>
<?php
    echo "打印3-10-3.txt文件中的前5行："."<br/>";
    $linecount = 1;
    $fh = fopen("3-10-3.txt","r");
    while(!feof($fh) && $linecount <= 5){
        $line = fgets($fh,4096);
        echo $linecount."&nbsp;".$line."<br/>";
        $linecount ++;
    }
?>

<h2>2.do...while</h2>
<?php
    $count = 11;
    do{
        echo "$count squared = ".pow($count,2)."<br/>";
        $count ++;
    }while($count < 10);
?>

<h2>3.for</h2>
<?php
    echo "<b>Example One</b>"."<br/>";
    for($kilometers = 1; $kilometers <= 5; $kilometers ++){
        echo "$kilometers kilometers = ".$kilometers * 0.62140." miles <br/>";
    }

    echo "<br/>";
    echo "<b>Example Two</b>"."<br/>";
    for($kilometers = 1; ; $kilometers ++){
        if($kilometers > 5) break;
        echo "$kilometers kilometers = ".$kilometers * 0.62140." miles <br/>";
    }

    echo "<br/>";
    echo "<b>Example Three</b>"."<br/>";
    $kilometers = 1;
    for(; ;){
        if ($kilometers > 5) break;
        echo "$kilometers kilometers = ".$kilometers * 0.62140." miles <br/>";
        $kilometers ++;
    }
?>

<h2>4.foreach</h2>
<?php
    $links = array(
        "www.apress.com",
        "www.php.net",
        "www.apache.org",
    );
    echo "<b>Online Resources</b>:<br/>";
    foreach ($links as $link){
        echo "<a href=\"http://$link\">$link</a><br/>";
    }
?>
<?php
    $links = array(
        "The Official Apache web site" => "www.apache.org",
        "The Apress corporate web site" => "www.apress.org",
        "The Official PHP web site" => "www.php.org",
    );
    echo "<b>Online Resources</b>:<br/>";
    foreach ($links as $title => $link){
        echo "<a href=\"http://$link\">$title</a>"."<br/>";
    }
?>

<h2>5.break</h2>
<?php
    $primes = array(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47);
    for($count = 1; $count ++; $count < 1000){
        $randomNumber = rand(1,50);
        if (in_array($randomNumber,$primes)){
            break;
        }
        else{
            echo "<p>Non-prime number encountered: $randomNumber</p>";
        }
    }
?>

<h2>6.continue</h2>
<?php
    $usernames = array(
        "grace",
        "doris",
        "gary",
        "nate",
        "missing",
        "tom",
    );
    for ($x = 0; $x < count($usernames); $x ++){
        if($usernames[$x] == "missing") continue;
        echo "Staff number: $usernames[$x] <br/>";
    }
?>
