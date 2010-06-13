<?php
error_reporting(E_WARNING | E_ERROR);    //显示警告和错误信息
echo $uvar;                        //这里产生注意信息，但不会显示出来
callFunc();                            //这里产生一个致命错误，并且会显示出来
?>