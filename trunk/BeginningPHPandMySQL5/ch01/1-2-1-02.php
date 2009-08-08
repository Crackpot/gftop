<?php
    $randomString = substr(md5(microtime()),0,5);
    echo "系统生成的5位随机字符串为：$randomString";
?>
