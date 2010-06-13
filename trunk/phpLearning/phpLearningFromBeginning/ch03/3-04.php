<?php
    session_start();

    $_SESSION['user'] = 'Crackpot';
    $_SESSION['explain']='这是3-04.php的session变量';
    echo '这个页面已经通过session保存了一些变量';
    echo '<br/><a href="3-05.php">进入3-05.php</a>查看这些变量值';
    echo '<br/>';
    echo '<br/><a href=".">返回目录</a>';
?>
